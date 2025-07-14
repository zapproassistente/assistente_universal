from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from fpdf import FPDF
from typing import Optional
import qrcode
from PIL import Image
import os
import io
import uuid

app = FastAPI()

# Pasta para PDFs temporários
PDF_DIR = "pdfs"
os.makedirs(PDF_DIR, exist_ok=True)

class PropostaData(BaseModel):
    profissao: str
    cliente: str
    servico: str
    valor: str
    vencimento: Optional[str] = ""
    termos: Optional[str] = ""
    assinatura_texto: Optional[str] = ""
    status: Optional[str] = "pendente"
    qrcode_pix: Optional[str] = ""
    modelo: Optional[str] = "personalizado"

def gerar_pdf(data: PropostaData, logo_bytes=None, assinatura_bytes=None, anexos=None, qr_bytes=None):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Logo
    if logo_bytes:
        with open("temp_logo.png", "wb") as f:
            f.write(logo_bytes)
        pdf.image("temp_logo.png", 10, 8, 40, 25)
        os.remove("temp_logo.png")

    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 15, "PROPOSTA / ORÇAMENTO / OS", ln=1, align="C")

    # Dados principais
    pdf.set_font("Arial", "", 13)
    pdf.cell(0, 10, f"Profissão: {data.profissao}", ln=1)
    pdf.cell(0, 10, f"Cliente: {data.cliente}", ln=1)
    pdf.cell(0, 10, f"Serviço: {data.servico}", ln=1)
    pdf.cell(0, 10, f"Valor: {data.valor}", ln=1)
    if data.vencimento:
        pdf.cell(0, 10, f"Vencimento: {data.vencimento}", ln=1)

    if data.termos:
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 10, "Termos / Observações:", ln=1)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, data.termos)

    # Anexos (fotos)
    if anexos:
        for idx, img_bytes in enumerate(anexos):
            img_file = f"temp_anexo_{idx}.png"
            with open(img_file, "wb") as f:
                f.write(img_bytes)
            pdf.add_page()
            pdf.image(img_file, 15, 40, 180, 120)
            os.remove(img_file)

    # QR Code PIX
    if qr_bytes:
        pdf.add_page()
        qr_file = "temp_qr.png"
        with open(qr_file, "wb") as f:
            f.write(qr_bytes)
        pdf.image(qr_file, 80, 50, 50, 50)
        pdf.set_y(105)
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Pague via PIX", align="C", ln=1)
        os.remove(qr_file)

    # Assinatura (imagem ou texto)
    pdf.set_y(-60)
    if assinatura_bytes:
        sign_file = "temp_sign.png"
        with open(sign_file, "wb") as f:
            f.write(assinatura_bytes)
        pdf.image(sign_file, 140, pdf.get_y(), 40, 25)
        os.remove(sign_file)
    elif data.assinatura_texto:
        pdf.set_font("Arial", "I", 13)
        pdf.cell(0, 10, f"Assinado eletronicamente por: {data.assinatura_texto}", ln=1, align="R")

    # Rodapé PRO
    pdf.set_y(-25)
    pdf.set_font("Arial", "I", 8)
    pdf.cell(0, 10, "Gerado com ZapPRO - https://zappro.site", align="C")

    # Salvar PDF
    file_id = str(uuid.uuid4())[:8]
    pdf_path = os.path.join(PDF_DIR, f"proposta_{file_id}.pdf")
    pdf.output(pdf_path)
    return pdf_path

def gerar_qr_pix(valor):
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(valor)
    img = qr.make_image(fill='black', back_color='white')
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    return buf.getvalue()

@app.post("/propostas/gerar")
async def criar_proposta(
    profissao: str = Form(...),
    cliente: str = Form(...),
    servico: str = Form(...),
    valor: str = Form(...),
    vencimento: str = Form(""),
    termos: str = Form(""),
    assinatura_texto: str = Form(""),
    status: str = Form("pendente"),
    modelo: str = Form("personalizado"),
    qrcode_pix: str = Form(""),
    logo: Optional[UploadFile] = File(None),
    assinatura: Optional[UploadFile] = File(None),
    anexos: Optional[list[UploadFile]] = None,
):
    logo_bytes = await logo.read() if logo else None
    assinatura_bytes = await assinatura.read() if assinatura else None
    anexos_bytes = [await a.read() for a in anexos] if anexos else None
    qr_bytes = gerar_qr_pix(qrcode_pix) if qrcode_pix else None

    data = PropostaData(
        profissao=profissao,
        cliente=cliente,
        servico=servico,
        valor=valor,
        vencimento=vencimento,
        termos=termos,
        assinatura_texto=assinatura_texto,
        status=status,
        modelo=modelo,
        qrcode_pix=qrcode_pix,
    )
    pdf_path = gerar_pdf(data, logo_bytes, assinatura_bytes, anexos_bytes, qr_bytes)
    pdf_url = f"/propostas/download/{os.path.basename(pdf_path)}"

    copy_pronta = f"""Olá, {cliente}!
Segue sua proposta/ordem de serviço gerada em PDF, personalizada para sua profissão ({profissao}).
{servico} | Valor: {valor}
Acesse, baixe ou imprima: {pdf_url}
Dúvidas, só chamar!"""

    return JSONResponse(content={"pdf_url": pdf_url, "copy_pronta": copy_pronta})

@app.get("/propostas/download/{pdf_file}")
async def baixar_pdf(pdf_file: str):
    pdf_path = os.path.join(PDF_DIR, pdf_file)
    if os.path.exists(pdf_path):
        return FileResponse(pdf_path, media_type="application/pdf", filename=pdf_file)
    return JSONResponse(content={"erro": "Arquivo não encontrado"}, status_code=404)

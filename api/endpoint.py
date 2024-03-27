from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import asyncio

app = FastAPI()

async def scan_operations(websocket: WebSocket):
    # Simulando 5 operações
    for i in range(1, 6):
        # Simula a operação
        await asyncio.sleep(2)  # Simula uma operação que leva 2 segundos
        # Envia atualização para o cliente
        await websocket.send_text(f"Operação {i} concluída")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await scan_operations(websocket)

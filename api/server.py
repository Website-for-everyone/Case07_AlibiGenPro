"""
AlibiGen Pro // FastAPI Backend & Image Evidence Generator
Case 07 — Y2K Retro OS Deadline Excuse & Fake Crash Evidence Studio
"""
import io
import random
from typing import Dict, Any
from pathlib import Path
from fastapi import FastAPI, Query, HTTPException, Response
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from PIL import Image, ImageDraw, ImageFont

app = FastAPI(title="AlibiGen Pro API", version="2.4.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent
WEB_DIR = BASE_DIR / "web"


class ExcuseRequest(BaseModel):
    recipient: str = "teamlead"
    absurdity: int = 35
    pity: int = 40
    tech: int = 85


VOCAB = {
    "greetings": {
        "client": ["Здравствуйте! Вынужден сообщить о непредвиденной задержке по проекту.", "Добрый день! К сожалению, релиз этапа сдвигается на пару часов.", "Приветствую. Возникли критические накладки со сдачей билда."],
        "teamlead": ["Привет! Слушай, мердж-реквест завис по независящим обстоятельствам.", "Привет, тимлид. Спринт пошел не по плану, срочный блокер.", "Хей, тут фатальный затык, не смогу закрыть тикет вовремя."],
        "boss": ["Добрый день. Докладываю о временной приостановке развертывания.", "Здравствуйте. По инфраструктуре возник нештатный инцидент."],
        "spouse": ["Любимая/любимый, я дико задерживаюсь, тут форс-мажор века!", "Солнце, прости пожалуйста, меня тут намертво заблокировало!"],
        "professor": ["Уважаемый преподаватель! Не могу вовремя сдать лабораторную работу."]
    },
    "tech": [
        "В магистральном BGP-маршрутизаторе провайдера произошел сбой синхронизации префиксов, из-за чего отвалился туннель к базе данных.",
        "В кластере Kubernetes начался каскадный OOMKilled в подах ingress-контроллера, вызванный утечкой дескрипторов сокетов.",
        "На локальном NVMe накопителе произошла деградация контроллера с переходом файловой системы ext4 в режим Read-Only.",
        "Контроллер питания материнской платы ушел в термозащиту из-за скачка фазы в домовой электросети.",
        "В libc произошел segmentation fault при вызове jemalloc, повредивший кэш сборщика мусора.",
        "Космическая частица вызвала инверсию бита (bitflip) в памяти ECC, заблокировав шину PCI Express."
    ],
    "pity": [
        "Вдобавок у соседей сверху лопнул стояк горячей воды, прямо сейчас стою в резиновых сапогах и держу ведро.",
        "К тому же меня экстренно вызвали к стоматологу из-за воспаления надкостницы и острой боли под анестезией.",
        "Параллельно у кота открылась аллергия, пришлось везти на ночную капельницу в круглосуточную ветеринарку.",
        "Глазной нерв спазмировало от 14 часов непрерывного сидения перед монитором, врач строго запретил смотреть на экраны.",
        "В подъезде срезали силовой кабель за долги управляющей компании, сижу без света и тепла на 4% аккумулятора."
    ],
    "absurd": [
        "А самое дикое — мой робот-пылесос сошел с ума, намотал провод зарядки ноутбука на щетку и застрял под диваном.",
        "Соседский попугай научился имитировать звук сигнализации и сидит прямо на моем балконе, невозможно сосредоточиться.",
        "Умный чайник взломали через уязвимость в протоколе Zigbee и начали DDoS-атаку на мой домашний роутер.",
        "Кот улегся прямо на клавишу Esc и перевел BIOS в режим циклического сброса настроек CMOS.",
        "Курьер доставки перепутал этажи и заблокировал мне входную дверь тремя мешками штукатурки."
    ],
    "closers": [
        "Уже поднял резервную копию и восстанавливаю окружение. До конца дня пришлю готовый результат!",
        "Прикладываю скриншот системного сбоя. Делаю всё возможное для стабилизации ситуации.",
        "Перезапускаю сервисы в безопасном режиме, спасибо за терпение и понимание!"
    ]
}


def build_excuse(recipient: str, absurdity: int, pity: int, tech: int) -> Dict[str, Any]:
    recipient_greetings = VOCAB["greetings"].get(recipient, VOCAB["greetings"]["teamlead"])
    greeting = random.choice(recipient_greetings)
    parts = []

    if tech > 20:
        parts.append(random.choice(VOCAB["tech"]))
    if pity > 25:
        parts.append(random.choice(VOCAB["pity"]))
    if absurdity > 30:
        parts.append(random.choice(VOCAB["absurd"]))

    if not parts:
        parts.append("Случилась неожиданная сетевая задержка при синхронизации репозитория.")

    closer = random.choice(VOCAB["closers"])
    full_text = f"{greeting} {' '.join(parts)} {closer}"

    score = 95 - (absurdity * 0.55) + (tech * 0.25) - (pity * 0.15)
    believability = max(12, min(99, int(score)))

    return {
        "text": full_text,
        "believability": believability,
        "recipient": recipient,
        "params": {
            "absurdity": absurdity,
            "pity": pity,
            "tech": tech
        }
    }


def generate_crash_image(preset: str, error_detail: str) -> bytes:
    width, height = 700, 400
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    if preset == "bsod":
        # Windows BSoD
        draw.rectangle([0, 0, width, height], fill="#0000AA")
        draw.rectangle([250, 40, 450, 65], fill="#C0C0C0")
        draw.text((320, 46), "Windows", fill="#0000AA")

        lines = [
            "A fatal exception 0E has occurred at 0028:C0011E36 in VXD VMM(01) +",
            "00010E36. The current application will be terminated.",
            f"* Error Context: {error_detail}",
            "",
            "* Press any key to terminate the current application.",
            "* Press CTRL+ALT+DEL again to restart your computer. You will",
            "  lose any unsaved information in all applications.",
            "",
            "*** STOP: 0x0000000A (0x00000002, 0x00000000, 0xF86B5A89, 0x80403D00)",
            "Memory dump complete. Contact your system administrator.",
            "Press any key to continue _"
        ]
        y = 90
        for line in lines:
            draw.text((40, y), line, fill="#FFFFFF")
            y += 22

    elif preset == "kernel_panic":
        draw.rectangle([0, 0, width, height], fill="#0A0A0A")
        lines = [
            "[   42.109823] Linux version 6.6.14-generic (buildd@sys-kernel-04)",
            "[   42.110291] CPU: 0 PID: 1337 Comm: rustc Tainted: G        W  O",
            f"[   42.111002] Kernel panic - not syncing: Fatal exception: {error_detail}",
            "[   42.111894] Hardware: AMD Threadripper / Micro-Star MS-7B09",
            "[   42.112450] Call Trace:",
            "[   42.112891]  <TASK>",
            "[   42.113245]  dump_stack_lvl+0x48/0x70",
            "[   42.113890]  panic+0x31a/0x360",
            "[   42.114789]  do_error_trap+0x6d/0xb0",
            "[   42.115781]  asm_exc_invalid_op+0x1a/0x20",
            "[   42.116240] RIP: 0010:jemalloc_page_fault+0x14/0x30",
            "[   42.117001] ---[ end Kernel panic: Unable to mount root fs ]---"
        ]
        y = 30
        for line in lines:
            color = "#FF5555" if "panic" in line else "#E0E0E0"
            draw.text((30, y), line, fill=color)
            y += 24

    elif preset == "gateway500":
        draw.rectangle([0, 0, width, height], fill="#F8F9FA")
        draw.text((50, 50), "502 Bad Gateway", fill="#212529")
        draw.line([(50, 90), (650, 90)], fill="#DEE2E6", width=2)
        draw.text((50, 120), "The server encountered a temporary error and could not complete your request.", fill="#495057")
        draw.text((50, 150), f"Incident: {error_detail}", fill="#495057")
        draw.text((50, 200), "Timestamp: UTC Synchronized Alert Event", fill="#6C757D")
        draw.text((50, 230), "Host: edge-router-prod-fra1.internal", fill="#6C757D")
        draw.line([(50, 310), (650, 310)], fill="#DEE2E6", width=2)
        draw.text((250, 335), "nginx/1.24.0 (Ubuntu Linux)", fill="#6C757D")

    else:  # Compiler trace
        draw.rectangle([0, 0, width, height], fill="#181818")
        draw.text((30, 40), "error[E0382]: use of moved value: `database_connection`", fill="#FF5555")
        draw.text((30, 70), "  --> src/controller/order_pipeline.rs:184:13", fill="#E0E0E0")
        draw.text((30, 95), "182| let database_connection = pool.acquire().await?;", fill="#E0E0E0")
        draw.text((30, 120), "183| spawn_worker_thread(database_connection);", fill="#E0E0E0")
        draw.text((30, 145), "184| database_connection.commit().await?;", fill="#FF5555")
        draw.text((30, 175), f"fatal error: {error_detail}", fill="#E0E0E0")
        draw.text((30, 210), "cargo build --release [FAILED]", fill="#55FF55")

    out_io = io.BytesIO()
    img.save(out_io, format="PNG")
    return out_io.getvalue()


@app.get("/health")
async def health_check():
    return {"status": "ok", "app": "AlibiGenPro", "version": "2.4.0"}


@app.post("/api/generate")
async def api_generate_excuse(req: ExcuseRequest):
    result = build_excuse(req.recipient, req.absurdity, req.pity, req.tech)
    return JSONResponse(content=result)


@app.get("/api/crash-image")
async def api_crash_image(
    preset: str = Query("bsod"),
    error_detail: str = Query("CRITICAL_PROCESS_DIED 0x000000EF")
):
    if preset not in ["bsod", "kernel_panic", "gateway500", "compiler"]:
        preset = "bsod"
    png_bytes = generate_crash_image(preset, error_detail)
    return Response(content=png_bytes, media_type="image/png")


if WEB_DIR.exists():
    app.mount("/", StaticFiles(directory=str(WEB_DIR), html=True), name="web")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8007, reload=False)

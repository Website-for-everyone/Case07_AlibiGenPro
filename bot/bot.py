"""
AlibiGen Pro // Telegram Companion Bot with Inline Mode (Aiogram 3.x)
Case 07 — Y2K Retro OS Deadline Excuse & Fake Evidence Studio
"""
import os
import io
import logging
from typing import List
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    Message,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    BufferedInputFile
)

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from api.server import build_excuse, generate_crash_image

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AlibiGenBot")

TOKEN = os.getenv("BOT_TOKEN", "TEST_TOKEN_ALIBIGEN")
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    text = (
        "🪟 **AlibiGen Pro 98 // Deadline Defender Bot**\n\n"
        "Я генерирую правдоподобные технические оправдания срывов дедлайнов "
        "и фабрикую скриншоты системных аварий (BSoD, Kernel Panic, 502 Gateway).\n\n"
        "💡 **Как использовать:**\n"
        "• **Инлайн-режим:** Введите в любом чате `@AlibiGenBot [слово]` для мгновенной отправки оправдания.\n"
        "• `/alibi [кому] [абсурд] [жалость] [техника]` — быстрая отмазка.\n"
        "• `/crash [bsod|panic|gateway500|compiler]` — получить скриншот поломки.\n"
    )
    await message.answer(text, parse_mode="Markdown")


@dp.message(Command("help"))
async def cmd_help(message: Message):
    text = (
        "🛠 **Команды AlibiGen Pro:**\n\n"
        "• `/alibi client 20 30 80` — сгенерировать текст для клиента с 80% тех-заумности.\n"
        "• `/crash bsod` — синий экран смерти Windows.\n"
        "• `/crash panic` — Linux Kernel Panic.\n"
        "• `/crash gateway500` — HTTP 502/500 Bad Gateway.\n"
        "• `/crash compiler` — фатальная ошибка компиляции.\n"
        "• Также доступен инлайн-режим в любом групповом чате!"
    )
    await message.answer(text, parse_mode="Markdown")


@dp.message(Command("alibi"))
async def cmd_alibi(message: Message):
    args = message.text.split()[1:]
    recipient = args[0] if len(args) > 0 else "teamlead"
    absurd = int(args[1]) if len(args) > 1 and args[1].isdigit() else 35
    pity = int(args[2]) if len(args) > 2 and args[2].isdigit() else 40
    tech = int(args[3]) if len(args) > 3 and args[3].isdigit() else 85

    res = build_excuse(recipient, absurd, pity, tech)
    response_text = (
        f"📝 **Отмазка для [{res['recipient'].upper()}]:**\n\n"
        f"\"{res['text']}\"\n\n"
        f"📊 **Правдоподобие:** {res['believability']}%"
    )
    await message.answer(response_text, parse_mode="Markdown")


@dp.message(Command("crash"))
async def cmd_crash(message: Message):
    args = message.text.split()[1:]
    preset = args[0].lower() if args else "bsod"
    if preset not in ["bsod", "panic", "gateway500", "compiler"]:
        preset = "bsod"

    png_bytes = generate_crash_image(preset, f"INCIDENT_{message.from_user.id}")
    file = BufferedInputFile(png_bytes, filename=f"crash_{preset}.png")
    await message.answer_photo(
        photo=file,
        caption=f"📸 **Скриншот сбоя [{preset.upper()}]** готов для отправки в рабочий чат."
    )


# Telegram Inline Mode (@AlibiGenBot)
@dp.inline_query()
async def inline_excuses(query: InlineQuery):
    q = query.query.strip().lower()
    recipients = ["teamlead", "client", "boss", "spouse"]
    target_rec = "teamlead"

    for r in recipients:
        if r in q:
            target_rec = r
            break

    results: List[InlineQueryResultArticle] = []

    # Generate 5 contextual options
    variations = [
        {"title": "🔧 Высокотехнологичный BGP/K8s сбой", "absurd": 10, "pity": 15, "tech": 95},
        {"title": "🌊 Затопление + авария на подстанции", "absurd": 20, "pity": 85, "tech": 50},
        {"title": "🐈 Кот на клавиатуре + сброс BIOS", "absurd": 85, "pity": 40, "tech": 40},
        {"title": "⚡ Скачок фазы + перегрев NVMe", "absurd": 15, "pity": 30, "tech": 90},
        {"title": "🦷 Экстренная стоматология + зуб мудрости", "absurd": 10, "pity": 95, "tech": 10}
    ]

    for idx, var in enumerate(variations):
        excuse_data = build_excuse(target_rec, var["absurd"], var["pity"], var["tech"])
        text = excuse_data["text"]
        believability = excuse_data["believability"]

        results.append(
            InlineQueryResultArticle(
                id=f"alibi_{idx}_{target_rec}",
                title=var["title"],
                description=f"Правдоподобие: {believability}% • {text[:60]}...",
                input_message_content=InputTextMessageContent(
                    message_text=f"{text}\n\n_(Правдоподобие: {believability}%)_",
                    parse_mode="Markdown"
                )
            )
        )

    await query.answer(results, cache_time=5, is_personal=True)


async def run_bot():
    bot = Bot(token=TOKEN)
    logger.info("Starting AlibiGen Pro Bot with Inline Mode...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(run_bot())

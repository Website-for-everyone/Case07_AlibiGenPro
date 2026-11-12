// AlibiGen Pro // Y2K Retro OS & Evidence Generator
document.addEventListener('DOMContentLoaded', () => {
  // Elements
  const crtOverlay = document.getElementById('crtOverlay');
  const chkCrt = document.getElementById('chkCrt');
  const trayClock = document.getElementById('trayClock');

  const rngAbsurd = document.getElementById('rngAbsurd');
  const rngPity = document.getElementById('rngPity');
  const rngTech = document.getElementById('rngTech');
  const valAbsurd = document.getElementById('valAbsurd');
  const valPity = document.getElementById('valPity');
  const valTech = document.getElementById('valTech');
  const selRecipient = document.getElementById('selRecipient');
  const btnSynthesize = document.getElementById('btnSynthesize');
  const txtExcuse = document.getElementById('txtExcuse');
  const meterFill = document.getElementById('meterFill');
  const believabilityVal = document.getElementById('believabilityVal');
  const btnCopy = document.getElementById('btnCopy');

  const selPreset = document.getElementById('selPreset');
  const txtCustomError = document.getElementById('txtCustomError');
  const evidenceCanvas = document.getElementById('evidenceCanvas');
  const btnRefreshCanvas = document.getElementById('btnRefreshCanvas');
  const btnDownloadEvidence = document.getElementById('btnDownloadEvidence');

  // Clock Ticker
  function updateClock() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const mins = String(now.getMinutes()).padStart(2, '0');
    trayClock.textContent = `${hours}:${mins}`;
  }
  setInterval(updateClock, 1000);
  updateClock();

  // CRT Scanline Toggle
  chkCrt.addEventListener('change', (e) => {
    if (e.target.checked) crtOverlay.classList.remove('disabled');
    else crtOverlay.classList.add('disabled');
  });

  // Slider Badges
  rngAbsurd.addEventListener('input', (e) => valAbsurd.textContent = `${e.target.value}%`);
  rngPity.addEventListener('input', (e) => valPity.textContent = `${e.target.value}%`);
  rngTech.addEventListener('input', (e) => valTech.textContent = `${e.target.value}%`);

  // Draggable Window Manager
  function makeWindowDraggable(winEl) {
    const titlebar = winEl.querySelector('.win-titlebar');
    let isDragging = false;
    let offsetX = 0, offsetY = 0;

    titlebar.addEventListener('mousedown', (e) => {
      isDragging = true;
      offsetX = e.clientX - winEl.offsetLeft;
      offsetY = e.clientY - winEl.offsetTop;
      document.querySelectorAll('.win98-window').forEach(w => w.style.zIndex = 10);
      winEl.style.zIndex = 20;
    });

    document.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      let newX = e.clientX - offsetX;
      let newY = e.clientY - offsetY;
      // Viewport bounds
      newX = Math.max(0, Math.min(window.innerWidth - winEl.offsetWidth, newX));
      newY = Math.max(0, Math.min(window.innerHeight - winEl.offsetHeight - 30, newY));
      winEl.style.left = `${newX}px`;
      winEl.style.top = `${newY}px`;
    });

    document.addEventListener('mouseup', () => isDragging = false);
  }

  document.querySelectorAll('.win98-window').forEach(makeWindowDraggable);

  // Procedural Excuse Generator Engine
  const vocab = {
    greetings: {
      client: ["Здравствуйте! Вынужден сообщить о непредвиденной задержке по проекту.", "Добрый день! К сожалению, релиз этапа сдвигается на пару часов.", "Приветствую. Возникли критические накладки со сдачей билда."],
      teamlead: ["Привет! Слушай, мердж-реквест завис по независящим обстоятельствам.", "Привет, тимлид. Спринт пошел не по плану, срочный блокер.", "Хей, тут фатальный затык, не смогу закрыть тикет вовремя."],
      boss: ["Добрый день. Докладываю о временной приостановке развертывания.", "Здравствуйте. По инфраструктуре возник нештатный инцидент."],
      spouse: ["Любимая/любимый, я дико задерживаюсь, тут форс-мажор века!", "Солнце, прости пожалуйста, меня тут намертво заблокировало!"],
      professor: ["Уважаемый преподаватель! Не могу вовремя сдать лабораторную работу."]
    },
    techPiles: [
      "В магистральном BGP-маршрутизаторе провайдера произошел сбой синхронизации префиксов, из-за чего отвалился туннель к базе данных.",
      "В кластере Kubernetes начался каскадный OOMKilled в подах ingress-контроллера, вызванный утечкой дескрипторов сокетов.",
      "На локальном NVMe накопителе произошла деградация контроллера с переходом файловой системы ext4 в режим Read-Only.",
      "Контроллер питания материнской платы ушел в термозащиту из-за скачка фазы в домовой электросети.",
      "В libc произошел segmentation fault при вызове jemalloc, повредивший кэш сборщика мусора.",
      "Космическая частица вызвала инверсию бита (bitflip) в памяти ECC, заблокировав шину PCI Express."
    ],
    pityPiles: [
      "Вдобавок у соседей сверху лопнул стояк горячей воды, прямо сейчас стою в резиновых сапогах и держу ведро.",
      "К тому же меня экстренно вызвали к стоматологу из-за воспаления надкостницы и острой боли под анестезией.",
      "Параллельно у кота открылась аллергия, пришлось везти на ночную капельницу в круглосуточную ветеринарку.",
      "Глазной нерв спазмировало от 14 часов непрерывного сидения перед монитором, врач строго запретил смотреть на экраны.",
      "В подъезде срезали силовой кабель за долги управляющей компании, сижу без света и тепла на 4% аккумулятора."
    ],
    absurdPiles: [
      "А самое дикое — мой робот-пылесос сошел с ума, намотал провод зарядки ноутбука на щетку и застрял под диваном.",
      "Соседский попугай научился имитировать звук сигнализации и сидит прямо на моем балконе, невозможно сосредоточиться.",
      "Умный чайник взломали через уязвимость в протоколе Zigbee и начали DDoS-атаку на мой домашний роутер.",
      "Кот улегся прямо на клавишу Esc и перевел BIOS в режим циклического сброса настроек CMOS.",
      "Курьер доставки перепутал этажи и заблокировал мне входную дверь тремя мешками штукатурки."
    ],
    closers: [
      "Уже поднял резервную копию и восстанавливаю окружение. До конца дня пришлю готовый результат!",
      "Прикладываю скриншот системного сбоя. Делаю всё возможное для стабилизации ситуации.",
      "Перезапускаю сервисы в безопасном режиме, спасибо за терпение и понимание!"
    ]
  };

  function synthesizeExcuse() {
    const recipient = selRecipient.value;
    const absurd = parseInt(rngAbsurd.value, 10);
    const pity = parseInt(rngPity.value, 10);
    const tech = parseInt(rngTech.value, 10);

    const greetingList = vocab.greetings[recipient] || vocab.greetings.teamlead;
    const greeting = greetingList[Math.floor(Math.random() * greetingList.length)];

    let bodyParts = [];

    if (tech > 20) {
      const techChoice = vocab.techPiles[Math.floor(Math.random() * vocab.techPiles.length)];
      bodyParts.push(techChoice);
    }

    if (pity > 25) {
      const pityChoice = vocab.pityPiles[Math.floor(Math.random() * vocab.pityPiles.length)];
      bodyParts.push(pityChoice);
    }

    if (absurd > 30) {
      const absurdChoice = vocab.absurdPiles[Math.floor(Math.random() * vocab.absurdPiles.length)];
      bodyParts.push(absurdChoice);
    }

    if (bodyParts.length === 0) {
      bodyParts.push("Случилась неожиданная сетевая задержка при выкатке репозитория на продакшн сервер.");
    }

    const closer = vocab.closers[Math.floor(Math.random() * vocab.closers.length)];
    const finalExcuse = `${greeting} ${bodyParts.join(' ')} ${closer}`;

    txtExcuse.value = finalExcuse;

    // Believability Metric
    let score = 95 - (absurd * 0.55) + (tech * 0.25) - (pity * 0.15);
    score = Math.max(12, Math.min(99, Math.round(score)));
    believabilityVal.textContent = `${score}%`;
    meterFill.style.width = `${score}%`;
    meterFill.style.backgroundColor = score > 60 ? '#008000' : (score > 35 ? '#CC8800' : '#CC0000');
  }

  btnSynthesize.addEventListener('click', synthesizeExcuse);
  synthesizeExcuse();

  btnCopy.addEventListener('click', () => {
    navigator.clipboard.writeText(txtExcuse.value).then(() => {
      btnCopy.textContent = 'СКОПИРОВАНО!';
      setTimeout(() => btnCopy.textContent = 'КОПИРОВАТЬ', 1500);
    });
  });

  // Evidence Studio Canvas Renderer
  function renderEvidence() {
    const ctx = evidenceCanvas.getContext('2d');
    const w = evidenceCanvas.width;
    const h = evidenceCanvas.height;
    const preset = selPreset.value;
    const customErr = txtCustomError.value || "FATAL_ERROR_0x000000EF";

    ctx.clearRect(0, 0, w, h);

    if (preset === 'bsod') {
      // Windows Blue Screen of Death
      ctx.fillStyle = '#0000AA';
      ctx.fillRect(0, 0, w, h);

      ctx.fillStyle = '#C0C0C0';
      ctx.fillRect(180, 40, 240, 24);
      ctx.fillStyle = '#0000AA';
      ctx.font = 'bold 16px monospace';
      ctx.fillText('Windows', 260, 58);

      ctx.fillStyle = '#FFFFFF';
      ctx.font = '13px monospace';
      ctx.fillText('A fatal exception 0E has occurred at 0028:C0011E36 in VXD VMM(01) +', 30, 90);
      ctx.fillText('00010E36. The current application will be terminated.', 30, 110);
      ctx.fillText(`* Cause: ${customErr}`, 30, 140);
      ctx.fillText('* Press any key to terminate the current application.', 30, 180);
      ctx.fillText('* Press CTRL+ALT+DEL again to restart your computer. You will', 30, 200);
      ctx.fillText('  lose any unsaved information in all applications.', 30, 220);
      ctx.fillText('*** STOP: 0x0000000A (0x00000002, 0x00000000, 0xF86B5A89, 0x80403D00)', 30, 260);
      ctx.fillText('Physical memory dump complete. Contact your system administrator.', 30, 290);
      ctx.fillText('Press any key to continue _', 30, 330);
    }
    else if (preset === 'kernel_panic') {
      // Linux Kernel Panic
      ctx.fillStyle = '#0A0A0A';
      ctx.fillRect(0, 0, w, h);

      ctx.fillStyle = '#E0E0E0';
      ctx.font = '12px monospace';
      ctx.fillText('[   42.109823] Linux version 6.6.14-generic (buildd@sys-kernel-04)', 20, 30);
      ctx.fillText('[   42.110291] CPU: 0 PID: 1337 Comm: rustc Tainted: G        W  O', 20, 50);
      ctx.fillStyle = '#FF5555';
      ctx.fillText(`[   42.111002] Kernel panic - not syncing: Fatal exception: ${customErr}`, 20, 75);
      ctx.fillStyle = '#E0E0E0';
      ctx.fillText('[   42.111894] Hardware name: AMD Ryzen Threadripper / Micro-Star MS-7B09', 20, 100);
      ctx.fillText('[   42.112450] Call Trace:', 20, 125);
      ctx.fillText('[   42.112891]  <TASK>', 20, 145);
      ctx.fillText('[   42.113245]  dump_stack_lvl+0x48/0x70', 20, 165);
      ctx.fillText('[   42.113890]  panic+0x31a/0x360', 20, 185);
      ctx.fillText('[   42.114210]  do_trap+0xd0/0x100', 20, 205);
      ctx.fillText('[   42.114789]  do_error_trap+0x6d/0xb0', 20, 225);
      ctx.fillText('[   42.115201]  exc_invalid_op+0x51/0x70', 20, 245);
      ctx.fillText('[   42.115781]  asm_exc_invalid_op+0x1a/0x20', 20, 265);
      ctx.fillText('[   42.116240] RIP: 0010:jemalloc_page_fault+0x14/0x30', 20, 285);
      ctx.fillStyle = '#FFFF55';
      ctx.fillText('[   42.117001] ---[ end Kernel panic - not syncing: VFS: Unable to mount root fs ]---', 20, 320);
    }
    else if (preset === 'gateway500') {
      // 502 / 500 Bad Gateway
      ctx.fillStyle = '#F8F9FA';
      ctx.fillRect(0, 0, w, h);

      ctx.fillStyle = '#212529';
      ctx.font = 'bold 36px sans-serif';
      ctx.fillText('502 Bad Gateway', 60, 90);

      ctx.strokeStyle = '#DEE2E6';
      ctx.beginPath();
      ctx.moveTo(60, 120);
      ctx.lineTo(540, 120);
      ctx.stroke();

      ctx.font = '14px sans-serif';
      ctx.fillStyle = '#495057';
      ctx.fillText('The server encountered a temporary error and could not complete your request.', 60, 155);
      ctx.fillText(`Error Details: ${customErr}`, 60, 185);

      ctx.font = '12px monospace';
      ctx.fillStyle = '#6C757D';
      const now = new Date().toUTCString();
      ctx.fillText(`Timestamp: ${now}`, 60, 230);
      ctx.fillText(`Client IP: 178.62.204.${Math.floor(Math.random() * 200 + 10)}`, 60, 250);
      ctx.fillText(`Ray ID: 85d1e${Math.random().toString(16).substring(2, 10)} (Cloudflare)`, 60, 270);
      ctx.fillText('Server Host: edge-router-prod-fra1.internal', 60, 290);

      ctx.strokeStyle = '#DEE2E6';
      ctx.beginPath();
      ctx.moveTo(60, 310);
      ctx.lineTo(540, 310);
      ctx.stroke();

      ctx.font = '13px sans-serif';
      ctx.fillText('nginx/1.24.0 (Ubuntu Linux)', 220, 335);
    }
    else if (preset === 'compiler') {
      // Compiler Fatal Error
      ctx.fillStyle = '#181818';
      ctx.fillRect(0, 0, w, h);

      ctx.fillStyle = '#FF5555';
      ctx.font = 'bold 13px monospace';
      ctx.fillText('error[E0382]: use of moved value: `database_connection`', 20, 40);

      ctx.fillStyle = '#E0E0E0';
      ctx.font = '12px monospace';
      ctx.fillText('  --> src/controller/order_pipeline.rs:184:13', 20, 65);
      ctx.fillText('   |', 20, 85);
      ctx.fillText('182|     let database_connection = pool.acquire().await?;', 20, 105);
      ctx.fillText('   |         ------------------- move occurs because value has type `PgConn`', 20, 125);
      ctx.fillText('183|     spawn_worker_thread(database_connection);', 20, 145);
      ctx.fillText('   |                         ------------------- value moved here', 20, 165);
      ctx.fillStyle = '#FF5555';
      ctx.fillText('184|     database_connection.commit_transaction().await?;', 20, 185);
      ctx.fillText('   |     ^^^^^^^^^^^^^^^^^^^ value used here after move', 20, 205);
      ctx.fillStyle = '#E0E0E0';
      ctx.fillText('   |', 20, 225);
      ctx.fillText(`fatal error: ${customErr}`, 20, 255);
      ctx.fillText('compilation terminated with status code 101.', 20, 275);
      ctx.fillStyle = '#55FF55';
      ctx.fillText('cargo build --release --locked [FAILED in 3m 42s]', 20, 315);
    }
  }

  btnRefreshCanvas.addEventListener('click', renderEvidence);
  selPreset.addEventListener('change', renderEvidence);
  txtCustomError.addEventListener('input', renderEvidence);
  renderEvidence();

  // Download Evidence PNG
  btnDownloadEvidence.addEventListener('click', () => {
    const dataUrl = evidenceCanvas.toDataURL('image/png');
    const a = document.createElement('a');
    a.href = dataUrl;
    a.download = `crash_evidence_${selPreset.value}.png`;
    a.click();
  });
});

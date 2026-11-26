// "Now in development" section on the home page.
// To post a devlog entry: add it to the top of `entries` and run `npm run build`.
// `date` is ISO (YYYY-MM-DD); the newest entry also drives the "Updated" label.
export const current = {
  title: 'Three Nights in Whitechapel',
  genre: ['Detective RPG · Whitechapel, 1888 · Unreal Engine 5', 'Детективная RPG · Уайтчепел, 1888 · Unreal Engine 5'],
  intro: [
    'A detective RPG I am building solo, from design to C++ code. My focus is on systems that turn an investigation into player decisions:',
    'Детективная RPG, которую я делаю один, от дизайна до кода на C++. Мой фокус — системы, которые превращают расследование в решения игрока:'
  ],
  points: [
    [['Fact system:', 'the game remembers every find and every dialogue answer and changes the world from night to night.'],
     ['Система фактов:', 'игра помнит каждую находку и каждый ответ в диалоге и меняет мир от ночи к ночи.']],
    [['2d6 checks:', 'before each roll you see which clues and choices give a bonus.'],
     ['Проверки 2d6:', 'перед броском видно, какие улики и выборы дают бонус.']],
    [['Reconstruction:', 'in the evening the hero tells his own version of events, and the scene replays from his words.'],
     ['Реконструкция:', 'вечером герой сам рассказывает версию событий, и сцена проигрывается по его словам.']]
  ],
  meta: [
    [['Role', 'solo development'], ['Роль', 'соло-разработка']],
    [['Engine', 'Unreal Engine 5, C++'], ['Движок', 'Unreal Engine 5, C++']],
    [['Bachelor project', ''], ['Бакалаврский проект', '']]
  ],
  tags: ['Unreal Engine 5', 'C++', 'Systems Design', 'Narrative Design', 'Level Design'],
  teaser: {
    src: 'tniw-teaser.mp4', poster: 'tniw-teaser-poster.jpg', width: 1280, height: 720,
    label: ['Three Nights in Whitechapel teaser', 'Тизер Three Nights in Whitechapel'],
    caption: ['Teaser', 'Тизер'],
    credit: ['Music: “Antigone” by Justin Allan Arnold, CC BY 4.0', 'Музыка: «Antigone», Justin Allan Arnold, CC BY 4.0']
  },
  // Screenshots: the first one is shown large, the rest as thumbnails below it.
  // `src` is one file for both languages, or [en, ru] when the shot has in-game text.
  images: [
    {src: ['tniw-partner-en.jpg', 'tniw-partner-ru.jpg'], width: 1500, height: 653,
     caption: ['Day 1: the partner asks where you served before the Yard — your answer picks your background and skills.', 'День 1: напарник спрашивает, где вы служили до Ярда, — ответ задаёт прошлое героя и его навыки.'],
     alt: ['Dialogue with the partner; on the left, a background card with three skills and their values', 'Диалог с напарником; слева карточка прошлого с тремя навыками и их значениями']},
    {src: 'tniw-map.jpg', width: 1500, height: 804,
     caption: ['The district map in the case book, drawn after Charles Booth’s 1889 poverty maps.', 'Карта района в деле — по картам бедности Чарльза Бута 1889 года.'],
     alt: ['An open notebook with a hand-hatched map of the district: the dosshouse, the pub, the barnyard and the workhouse yard, with handwritten notes and the player’s position marker', 'Раскрытая записная книжка с заштрихованной от руки картой района: ночлежка, паб, скотный двор и двор работного дома, рукописные пометки и метка игрока']},
    {src: ['tniw-magpie-en.jpg', 'tniw-magpie-ru.jpg'], width: 1500, height: 653,
     caption: ['Magpie eavesdrops from the dosshouse stairs.', 'Мегпай подслушивает с лестницы ночлежки.'],
     alt: ['Eavesdropping: a view through the stair railings at two figures below, with the overheard lines in a panel', 'Подслушивание: вид сквозь перила лестницы на двоих внизу, подслушанные реплики на панели']},
    {src: 'tniw-prologue.jpg', width: 1280, height: 720,
     caption: ['Prologue: a foggy Whitechapel passage at night.', 'Пролог: ночной проход в Уайтчепеле в тумане.'],
     alt: ['A figure crawls along a dark, foggy passage towards a distant lamp', 'Фигура ползёт по тёмному туманному проходу к далёкому фонарю']},
    {src: 'tniw-menu.jpg', width: 1280, height: 720,
     caption: ['Main menu — The Illustrated Police News, 22 September 1888.', 'Главное меню — выпуск The Illustrated Police News от 22 сентября 1888 года.'],
     alt: ['Main menu: an 1888 Illustrated Police News front page with engravings and the New Game and Load Game items', 'Главное меню: газетная полоса The Illustrated Police News 1888 года с гравюрами и пунктами New Game и Load Game']}
  ],
  // status: done | now | next
  stages: [
    {status: 'done', name: ['S1 · Foundation', 'S1 · Основа'], note: ['2–8 Nov', '2–8 нояб.']},
    {status: 'done', name: ['S2 · Prototype 1', 'S2 · Прототип 1'], note: ['night 1 playable', 'ночь 1 играбельна']},
    {status: 'done', name: ['S3 · Prototype 2', 'S3 · Прототип 2'], note: ['shown 23 Nov', 'показ 23.11']},
    {status: 'now', name: ['S4 · Feature cut', 'S4 · Срез фич'], note: ['23–29 Nov', '23–29 нояб.']},
    {status: 'next', name: ['Polish', 'Полировка'], note: ['text, sound, light', 'тексты, звук, свет']},
    {status: 'next', name: ['Submission', 'Сдача'], note: ['28 Dec', '28.12']}
  ],
  currentStage: ['sprint 4 · feature cut', 'спринт 4 · срез фич']
};

// kind: level | design | playtest | milestone
export const entries = [
  {date: '2026-11-26', kind: 'level', text: ['Paved and lit the district: single setts, a ringed plaza, puddles, gas lamps and weather. The stockyard gate now swings open.', 'Район замощён и освещён: брусчатка, круглая площадь, лужи, газовые фонари и погода. Ворота скотного двора теперь открываются.']},
  {date: '2026-11-25', kind: 'design', text: ['Newspaper-style menus: settings and sound open as newspaper windows, and the pause menu is a pile of clippings.', 'Меню в газетном стиле: настройки и звук открываются газетными окнами, а пауза — стопка вырезок.']},
  {date: '2026-11-25', kind: 'design', text: ['The first reconstruction now teaches itself: walk the yard, and the partner writes down the first link.', 'Первая реконструкция теперь обучает сама: пройдитесь по двору — и напарник запишет первое звено.']},
  {date: '2026-11-25', kind: 'level', text: ['Detailed blockouts of the pawnshop, the laundry and the carpenter’s workshop.', 'Детальные блок-ауты ломбарда, прачечной и мастерской столяра.']},
  {date: '2026-11-23', kind: 'playtest', text: ['Playtest 23.11: reworked Magpie’s day route and the voices behind the wall; rooms now stay dark from outside.', 'Плейтест 23.11: переделаны маршрут дня Мегпай и голоса за стеной, комнаты снаружи теперь тёмные.']},
  {date: '2026-11-23', kind: 'milestone', text: ['Prototype 2: the whole game runs as a skeleton from New Game to the ending; an automated test walks the routes through it.', 'Прототип 2: вся игра проходится каркасом от «Новой игры» до финала, автотест проверяет маршруты прохождения.']},
  {date: '2026-11-22', kind: 'level', text: ['Blockout gave way to interiors: the dosshouse, the gambling den “The Burrow”, the pub’s back yard.', 'Блок-аут уступил место интерьерам: ночлежка, игорный дом «Нора», задний двор паба.']},
  {date: '2026-11-21', kind: 'design', text: ['New district map based on Charles Booth’s poverty maps: street classes and handwritten notes.', 'Новая карта района по картам бедности Чарльза Бута: классы улиц и пометки от руки.']},
  {date: '2026-11-20', kind: 'playtest', text: ['Searching the butcher’s became the strongest moment of the day. The evening reconstruction now plays piece by piece as the hero tells it.', 'Обыск у мясника стал самым сильным моментом дня. Вечерняя реконструкция теперь идёт по кускам — по мере рассказа героя.']},
  {date: '2026-11-20', kind: 'design', text: ['Magpie’s journal: a memory that helped in a roll is marked on the board.', 'Журнал Мегпай: воспоминание, которое помогло в броске, отмечается на доске.']},
  {date: '2026-11-19', kind: 'playtest', text: ['First playtest of day 1: removed unnecessary interface hints.', 'Первый плейтест дня 1: убраны лишние подсказки в интерфейсе.']},
  {date: '2026-11-16', kind: 'design', text: ['Interface frames and ornaments taken from 1880s magazines (CC0).', 'Рамки и орнаменты интерфейса — из журналов 1880-х (CC0).']}
];

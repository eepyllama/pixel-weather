// ============================================================
// PIXEL WEATHER — MOOD ENGINE (fixed)
// ============================================================

const ICON_TO_MOOD = {
    '01d': 'sunny',   '01n': 'night',
    '02d': 'cloudy',  '02n': 'night',
    '03d': 'cloudy',  '03n': 'night',
    '04d': 'cloudy',  '04n': 'night',
    '09d': 'rainy',   '09n': 'rainy',
    '10d': 'rainy',   '10n': 'rainy',
    '11d': 'stormy',  '11n': 'stormy',
    '13d': 'snow',    '13n': 'snow',
    '50d': 'mist',    '50n': 'night',
};

const ICON_TO_EMOJI = {
    '01d': '☀️',  '01n': '🌙',
    '02d': '⛅',  '02n': '☁️',
    '03d': '☁️',  '03n': '☁️',
    '04d': '☁️',  '04n': '☁️',
    '09d': '🌦️', '09n': '🌧️',
    '10d': '🌧️', '10n': '🌧️',
    '11d': '⛈️', '11n': '⛈️',
    '13d': '❄️',  '13n': '❄️',
    '50d': '🌫️', '50n': '🌫️',
};

const MOOD_MESSAGES = {
    sunny:   '> CLEAR SKIES. PERFECT VISIBILITY.',
    cloudy:  '> OVERCAST. KEEP YOUR COMPASS CLOSE.',
    rainy:   '> RAINFALL DETECTED. SEEK SHELTER.',
    stormy:  '> STORM WARNING. ALL HANDS ON DECK.',
    snow:    '> SNOWFALL ACTIVE. TREAD CAREFULLY.',
    night:   '> NIGHT MODE. STARS ARE YOUR GUIDE.',
    mist:    '> LOW VISIBILITY. PROCEED WITH CAUTION.',
    default: '> AWAITING LOCATION DATA...',
};

const ALL_MOOD_CLASSES = [
    'mood-sunny','mood-cloudy','mood-rainy',
    'mood-stormy','mood-snow','mood-night',
    'mood-mist','mood-default'
];

// Typewriter — cancels any previous run via a closure flag
// Each call creates a new 'active' flag; old intervals
// check the flag and stop themselves automatically
function typewriter(el, text, speed) {
    // Clear immediately so old text never shows doubled
    el.textContent = '';

    let i = 0;

    // Using a named function instead of anonymous arrow
    // so we can cancel cleanly
    let cancelled = false;

    // Cancel any previous typewriter on this element
    // by storing a cancel function on the element itself
    if (el._cancelTypewriter) {
        el._cancelTypewriter();
    }

    el._cancelTypewriter = () => { cancelled = true; };

    function tick() {
        if (cancelled) return;
        if (i < text.length) {
            el.textContent += text[i];
            i++;
            setTimeout(tick, speed);
        }
    }

    tick();
}

function applyMood() {
    const iconCode = document.body.dataset.weather;
    const bgScene  = document.getElementById('bgScene');
    const msgText  = document.getElementById('messageText');

    const mood = ICON_TO_MOOD[iconCode] || 'default';

    // 1. Update body data-mood
    document.body.dataset.mood = mood;

    // 2. Switch background class
    if (bgScene) {
        ALL_MOOD_CLASSES.forEach(c => bgScene.classList.remove(c));
        bgScene.classList.add(`mood-${mood}`);
    }

    // 3. Typewriter message — single call, self-cancelling
    if (msgText) {
        const message = MOOD_MESSAGES[mood] || MOOD_MESSAGES.default;
        typewriter(msgText, message, 45);
    }
}

function applyWeatherIcon() {
    const iconCode = document.body.dataset.weather;
    const iconBox  = document.getElementById('pixelIcon');

    if (iconBox && iconCode) {
        const emoji = ICON_TO_EMOJI[iconCode] || '🌡️';
        // Set textContent directly — no CSS ::before trickery
        // This is simpler and more reliable across browsers
        iconBox.textContent = emoji;
    }
}

function applyForecastIcons() {
    const cards = document.querySelectorAll('.forecast-icon');
    cards.forEach(el => {
        const code = el.dataset.icon;
        el.textContent = ICON_TO_EMOJI[code] || '🌡️';
    });
}

// ONE single DOMContentLoaded listener — the root fix for the double bug
document.addEventListener('DOMContentLoaded', function() {
    applyMood();
    applyWeatherIcon();
    applyForecastIcons();
});
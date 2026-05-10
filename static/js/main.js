// Phase 3: Dynamic behaviour will live here
// ============================================================
// PIXEL WEATHER — MOOD ENGINE
// Reads the weather icon code, applies the correct:
//   - background scene class
//   - body data-mood attribute  
//   - pixel icon class
//   - flavour message
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

const ICON_TO_CLASS = {
    '01d': 'icon-clear-day',
    '01n': 'icon-clear-night',
    '02d': 'icon-cloudy',    '02n': 'icon-cloudy',
    '03d': 'icon-overcast',  '03n': 'icon-overcast',
    '04d': 'icon-overcast',  '04n': 'icon-overcast',
    '09d': 'icon-drizzle',   '09n': 'icon-drizzle',
    '10d': 'icon-rainy',     '10n': 'icon-rainy',
    '11d': 'icon-stormy',    '11n': 'icon-stormy',
    '13d': 'icon-snow',      '13n': 'icon-snow',
    '50d': 'icon-mist',      '50n': 'icon-mist',
};

const MOOD_MESSAGES = {
    sunny:  '> CLEAR SKIES. PERFECT VISIBILITY. ADVENTURE AWAITS.',
    cloudy: '> OVERCAST. KEEP YOUR COMPASS CLOSE.',
    rainy:  '> RAINFALL DETECTED. SEEK SHELTER OR SAIL THROUGH.',
    stormy: '> STORM WARNING. ALL HANDS ON DECK.',
    snow:   '> SNOWFALL ACTIVE. TREAD CAREFULLY, TRAVELLER.',
    night:  '> NIGHT MODE. STARS ARE YOUR NAVIGATION.',
    mist:   '> LOW VISIBILITY. PROCEED WITH CAUTION.',
    default:'> AWAITING LOCATION DATA...',
};

// All possible mood class names — we remove all before adding one
const ALL_MOODS = ['mood-sunny','mood-cloudy','mood-rainy',
                   'mood-stormy','mood-snow','mood-night',
                   'mood-mist','mood-default'];

function applyMood() {
    const iconCode  = document.body.dataset.weather;
    const bgScene   = document.getElementById('bgScene');
    const iconBox   = document.getElementById('pixelIcon');
    const msgText   = document.getElementById('messageText');

    // Determine mood — fallback to 'default' if icon not recognised
    const mood = ICON_TO_MOOD[iconCode] || 'default';

    // 1. Update body data-mood (used by CSS snow overrides)
    document.body.dataset.mood = mood;

    // 2. Switch background scene class
    if (bgScene) {
        ALL_MOODS.forEach(cls => bgScene.classList.remove(cls));
        bgScene.classList.add(`mood-${mood}`);
    }

    // 3. Apply pixel icon class
    if (iconBox) {
        // Remove all existing icon classes
        iconBox.className = 'pixel-weather-icon';
        const iconClass = ICON_TO_CLASS[iconCode];
        if (iconClass) {
            iconBox.classList.add(iconClass);
        }
    }

    // 4. Set the flavour message with typewriter effect
    if (msgText) {
        const message = MOOD_MESSAGES[mood] || MOOD_MESSAGES.default;
        typewriter(msgText, message, 40);
    }
}

// Typewriter effect — prints text one character at a time.
// 'el' is the DOM element, 'text' is the full string,
// 'speed' is milliseconds per character.
function typewriter(el, text, speed) {
    el.textContent = '';
    let i = 0;

    function tick() {
        if (i < text.length) {
            el.textContent += text[i];
            i++;
            setTimeout(tick, speed);
        }
    }

    tick();
}

// Run everything once the page DOM is ready
document.addEventListener('DOMContentLoaded', applyMood);
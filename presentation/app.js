// HACCP Level 2 Interactive Presentation Masterclass Application
document.addEventListener("DOMContentLoaded", () => {
  const slides = window.HACCP_SLIDES_DATA || [];
  const renderers = window.HACCP_RENDERERS;
  let currentSlideIndex = 0;
  let isPlaying = false;
  let autoAdvance = true;
  let bgMusicOn = true;
  let subtitlesEnabled = true;

  // DOM Elements
  const stage = document.getElementById("stage");
  const viewport = document.getElementById("viewport");
  const voiceAudio = document.getElementById("voice-audio");
  const bgAudio = document.getElementById("bg-audio");
  const playBtn = document.getElementById("play-btn");
  const prevBtn = document.getElementById("prev-btn");
  const nextBtn = document.getElementById("next-btn");
  const slideSelect = document.getElementById("slide-select");
  const progressFill = document.getElementById("progress-fill");
  const timeDisplay = document.getElementById("time-display");
  const exportBtn = document.getElementById("export-btn");
  const fullscreenBtn = document.getElementById("fullscreen-btn");
  const musicToggleBtn = document.getElementById("music-toggle-btn");
  const subtitlesToggleBtn = document.getElementById("subtitles-toggle-btn");
  const subtitlesOverlay = document.getElementById("subtitles-overlay");
  const volumeMuteBtn = document.getElementById("volume-mute-btn");
  const volumeSlider = document.getElementById("volume-slider");
  const volumeGroup = document.querySelector(".volume-group");
  const audioVisualizer = document.getElementById("audio-visualizer");

  const stageCategory = document.getElementById("stage-category");
  const stageTitle = document.getElementById("stage-title");
  const stageSubtitle = document.getElementById("stage-subtitle");
  const stageContent = document.getElementById("stage-content");
  const stageCounter = document.getElementById("stage-counter");

  // Populate Dropdown
  slides.forEach((s, idx) => {
    const opt = document.createElement("option");
    opt.value = idx;
    opt.textContent = `Slide ${s.slide_num}: ${s.title}`;
    slideSelect.appendChild(opt);
  });

  // Stage Rescaling Math (1920x1080 fixed aspect ratio locked to viewport)
  function resizeStage() {
    const scale = Math.min(viewport.clientWidth / 1920, viewport.clientHeight / 1080) * 0.98;
    stage.style.transform = `scale(${scale})`;
  }
  window.addEventListener("resize", resizeStage);
  resizeStage();

  // Render Slide Content
  function loadSlide(index) {
    currentSlideIndex = index;
    slideSelect.value = index;
    const slide = slides[index];
    if (!slide) return;

    voiceAudio.src = slide.audio_file;
    voiceAudio.currentTime = 0;
    subtitlesOverlay.classList.add("is-hidden");

    if (stageCategory) stageCategory.textContent = slide.category;
    if (stageTitle) stageTitle.textContent = slide.title;
    if (stageSubtitle) stageSubtitle.textContent = slide.subtitle;
    if (stageCounter) stageCounter.textContent = `Slide ${String(slide.slide_num).padStart(2, "0")} / 26`;

    if (stageContent) {
      stageContent.classList.remove("slide-content-transition");
      void stageContent.offsetWidth;
      stageContent.innerHTML = renderers.renderContent(slide);
      stageContent.classList.add("slide-content-transition");
    }

    checkSynchronization();
    if (isPlaying) {
      voiceAudio.play().catch(() => {});
      if (bgMusicOn && bgAudio.paused) bgAudio.play().catch(() => {});
    }
  }

  // Real-Time Audio Synchronization & Subtitle Cue Tracking
  let progressBarBg; // set after DOM query below

  function checkSynchronization() {
    const t = voiceAudio.currentTime;
    const dur = voiceAudio.duration || 1;
    const slide = slides[currentSlideIndex];

    const pct = Math.min(100, (t / dur) * 100);
    progressFill.style.width = `${pct}%`;
    if (progressBarBg) progressBarBg.style.setProperty("--progress-pct", `${pct}%`);
    timeDisplay.textContent = `${formatTime(t)} / ${formatTime(dur)}`;

    if (subtitlesEnabled && slide && slide.subtitles) {
      const cue = slide.subtitles.find(c => t >= c.start && t < c.end);
      if (cue) {
        subtitlesOverlay.textContent = cue.text;
        subtitlesOverlay.classList.remove("is-hidden");
      } else {
        subtitlesOverlay.classList.add("is-hidden");
      }
    } else {
      subtitlesOverlay.classList.add("is-hidden");
    }

    const syncElements = stage.querySelectorAll("[data-start-time]");
    syncElements.forEach((el) => {
      const startTime = parseFloat(el.getAttribute("data-start-time"));
      const endTime = parseFloat(el.getAttribute("data-end-time") || "999");
      if (t >= startTime) el.classList.add("is-revealed");
      else el.classList.remove("is-revealed");

      if (t >= startTime && t < endTime) el.classList.add("is-active-speaker");
      else el.classList.remove("is-active-speaker");
    });
  }

  function formatTime(sec) {
    if (isNaN(sec)) return "00:00";
    const m = Math.floor(sec / 60);
    const s = Math.floor(sec % 60);
    return `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
  }

  let syncRafId = null;

  function startSyncLoop() {
    cancelSyncLoop();
    function syncFrame() {
      checkSynchronization();
      if (isPlaying && !voiceAudio.paused) {
        syncRafId = requestAnimationFrame(syncFrame);
      }
    }
    syncRafId = requestAnimationFrame(syncFrame);
  }

  function cancelSyncLoop() {
    if (syncRafId) {
      cancelAnimationFrame(syncRafId);
      syncRafId = null;
    }
  }

  // HELPER: update play button SVG icon & visualizer
  function setPlayIcon(playing) {
    playBtn.innerHTML = playing
      ? `<svg class="svg-icon icon-pause" viewBox="0 0 24 24" fill="currentColor"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>`
      : `<svg class="svg-icon icon-play" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>`;
    playBtn.classList.toggle("is-playing", playing);
    if (audioVisualizer) audioVisualizer.classList.toggle("is-paused", !playing);
  }

  voiceAudio.addEventListener("play", startSyncLoop);
  voiceAudio.addEventListener("pause", cancelSyncLoop);
  voiceAudio.addEventListener("timeupdate", checkSynchronization);

  voiceAudio.addEventListener("ended", () => {
    cancelSyncLoop();
    if (autoAdvance && currentSlideIndex < slides.length - 1) {
      loadSlide(currentSlideIndex + 1);
      if (isPlaying) {
        voiceAudio.play();
        if (bgMusicOn && bgAudio.paused) bgAudio.play().catch(() => {});
      }
    } else {
      isPlaying = false;
      bgAudio.pause();
      setPlayIcon(false);
    }
  });

  // Play / Pause Controls (Synchronized voice and background music)
  playBtn.addEventListener("click", () => {
    if (voiceAudio.paused) {
      voiceAudio.play();
      if (bgMusicOn) bgAudio.play().catch(() => {});
      isPlaying = true;
      setPlayIcon(true);
    } else {
      voiceAudio.pause();
      bgAudio.pause();
      isPlaying = false;
      setPlayIcon(false);
    }
  });

  prevBtn.addEventListener("click", () => {
    if (currentSlideIndex > 0) loadSlide(currentSlideIndex - 1);
  });

  nextBtn.addEventListener("click", () => {
    if (currentSlideIndex < slides.length - 1) loadSlide(currentSlideIndex + 1);
  });

  slideSelect.addEventListener("change", (e) => loadSlide(parseInt(e.target.value)));

  // Subtitles Toggle — class-based (no text labels)
  subtitlesToggleBtn.addEventListener("click", () => {
    subtitlesEnabled = !subtitlesEnabled;
    subtitlesToggleBtn.classList.toggle("is-active", subtitlesEnabled);
    if (!subtitlesEnabled) subtitlesOverlay.classList.add("is-hidden");
    else checkSynchronization();
  });

  // Background Music Toggle — class-based
  bgAudio.volume = 0.12;
  musicToggleBtn.addEventListener("click", () => {
    bgMusicOn = !bgMusicOn;
    musicToggleBtn.classList.toggle("is-active", bgMusicOn);
    if (bgMusicOn) {
      if (isPlaying) bgAudio.play().catch(() => {});
    } else {
      bgAudio.pause();
    }
  });

  // Voice Volume Slider + Mute Button
  const SVG_ATTRS = `class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"`;
  const VOL_ICON_ON = `<svg ${SVG_ATTRS}><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>`;
  const VOL_ICON_OFF = `<svg ${SVG_ATTRS}><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>`;
  let lastVolume = 1; voiceAudio.volume = 1;

  function updateVolumeUI() {
    const muted = voiceAudio.muted || voiceAudio.volume === 0;
    volumeMuteBtn.innerHTML = muted ? VOL_ICON_OFF : VOL_ICON_ON;
    volumeGroup.classList.toggle("is-muted", muted);
  }
  volumeSlider.addEventListener("input", () => {
    const val = parseFloat(volumeSlider.value);
    voiceAudio.volume = val;
    if (val > 0) { voiceAudio.muted = false; lastVolume = val; }
    updateVolumeUI();
  });
  volumeMuteBtn.addEventListener("click", () => {
    if (voiceAudio.muted || voiceAudio.volume === 0) {
      voiceAudio.muted = false; voiceAudio.volume = lastVolume || 1;
      volumeSlider.value = voiceAudio.volume;
    } else {
      lastVolume = voiceAudio.volume; voiceAudio.muted = true; volumeSlider.value = 0;
    }
    updateVolumeUI();
  });
  updateVolumeUI();

  fullscreenBtn.addEventListener("click", () => {
    if (!document.fullscreenElement) document.documentElement.requestFullscreen();
    else document.exitFullscreen();
  });

  // Progress Bar — Click & Drag to Seek
  progressBarBg = document.querySelector(".progress-bar-bg");

  function seekFromEvent(e) {
    const rect = progressBarBg.getBoundingClientRect();
    const ratio = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
    const dur = voiceAudio.duration;
    if (!isNaN(dur) && dur > 0) {
      voiceAudio.currentTime = ratio * dur;
      checkSynchronization();
    }
  }

  let isSeeking = false;
  progressBarBg.addEventListener("mousedown", (e) => {
    isSeeking = true;
    seekFromEvent(e);
  });
  window.addEventListener("mousemove", (e) => { if (isSeeking) seekFromEvent(e); });
  window.addEventListener("mouseup", () => { isSeeking = false; });

  // Single ZIP Export: Full Course MP4 Video + Verbatim Synchronized SRT
  exportBtn.addEventListener("click", () => {
    const a = document.createElement("a");
    a.href = "assets/export/HACCP_Level_2_Masterclass_Complete.zip";
    a.download = "HACCP_Level_2_Masterclass_Complete.zip";
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
  });

  // Keyboard Shortcuts
  document.addEventListener("keydown", (e) => {
    if (e.code === "Space") { e.preventDefault(); playBtn.click(); }
    else if (e.code === "ArrowRight") nextBtn.click();
    else if (e.code === "ArrowLeft") prevBtn.click();
    else if (e.code === "KeyF") fullscreenBtn.click();
    else if (e.code === "KeyM") volumeMuteBtn.click();
    else if (e.code === "KeyC") subtitlesToggleBtn.click();
  });

  setPlayIcon(false);
  loadSlide(0);
});

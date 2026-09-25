document.addEventListener('DOMContentLoaded', () => {
    
    // Sample Emails Dictionary
    const samples = {
        meeting: "Dear team,\n\nLet's schedule a meeting for tomorrow at 2:00 PM to discuss the new project roadmap. Please let me know if you are available.\n\nBest,\nSarah",
        job: "Hello,\n\nPlease find my resume attached for the Senior Software Engineer position. I am very excited about this opportunity and look forward to hearing from you.\n\nRegards,\nJohn Doe",
        complaint: "To whom it may concern,\n\nThe product I received yesterday is completely damaged. I demand a full refund immediately. This service is terrible.\n\n- Alex",
        support: "Hi Support Team,\n\nI forgot my password and cannot log into my dashboard. Can someone please help me reset it?\n\nThanks,\nMaria",
        personal: "Hey man, it was great seeing you last weekend. Are we still on for dinner next Friday at 8 PM?",
        finance: "Dear Customer,\n\nYour invoice #9942 for the amount of $150.00 is due on the 15th of next month. Please ensure timely payment.",
        spam: "CONGRATULATIONS!!! You have won a free iPhone 15! Click the link below to claim your prize now before it expires!"
    };

    const emailInput = document.getElementById('emailInput');
    const sampleSelect = document.getElementById('sampleEmails');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const clearBtn = document.getElementById('clearBtn');
    const toneSelect = document.getElementById('toneSelect');
    const copyBtn = document.getElementById('copyBtn');
    const regenBtn = document.getElementById('regenBtn');
    
    // Toast setup
    const toastEl = document.getElementById('liveToast');
    const toast = new bootstrap.Toast(toastEl);
    const toastMsg = document.getElementById('toastMessage');

    function showToast(message) {
        toastMsg.textContent = message;
        toast.show();
    }

    // Load sample email
    sampleSelect.addEventListener('change', (e) => {
        const val = e.target.value;
        if (val && samples[val]) {
            emailInput.value = samples[val];
        }
    });

    // Clear input
    clearBtn.addEventListener('click', () => {
        emailInput.value = '';
        document.getElementById('emptyState').classList.remove('d-none');
        document.getElementById('resultsContent').classList.add('d-none');
    });

    // Analyze Action
    analyzeBtn.addEventListener('click', async () => {
        const text = emailInput.value.trim();
        const tone = toneSelect.value;
        
        if (!text) {
            alert("Please enter an email before analyzing.");
            return;
        }

        // UI loading state
        const spinner = document.getElementById('loadingSpinner');
        spinner.classList.remove('d-none');
        analyzeBtn.disabled = true;

        try {
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: text, tone: tone })
            });
            
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || "Server error");
            }

            // Populate Results
            document.getElementById('resCategory').textContent = data.category;
            document.getElementById('resCatConf').textContent = data.category_confidence;
            
            const sentimentEl = document.getElementById('resSentiment');
            sentimentEl.textContent = data.sentiment;
            // Color coding sentiment
            sentimentEl.className = 'mb-1 ' + (data.sentiment === 'Positive' ? 'text-success' : (data.sentiment === 'Negative' ? 'text-danger' : 'text-info'));
            document.getElementById('resSentConf').textContent = data.sentiment_confidence;
            
            document.getElementById('resSummary').textContent = data.summary;
            document.getElementById('resReply').value = data.reply;

            // Render Entities
            const entitiesContainer = document.getElementById('resEntities');
            entitiesContainer.innerHTML = '';
            if (data.entities && data.entities.length > 0) {
                data.entities.forEach(ent => {
                    const badge = document.createElement('span');
                    badge.className = 'badge bg-secondary entity-badge';
                    badge.innerHTML = `<strong>${ent.type}:</strong> ${ent.value}`;
                    entitiesContainer.appendChild(badge);
                });
            } else {
                entitiesContainer.innerHTML = '<span class="text-muted fst-italic">No important entities detected.</span>';
            }

            // Show results
            document.getElementById('emptyState').classList.add('d-none');
            document.getElementById('resultsContent').classList.remove('d-none');
            
        } catch (error) {
            alert(error.message);
        } finally {
            spinner.classList.add('d-none');
            analyzeBtn.disabled = false;
        }
    });

    // Copy Reply
    copyBtn.addEventListener('click', () => {
        const replyText = document.getElementById('resReply');
        replyText.select();
        document.execCommand('copy');
        showToast("Reply copied to clipboard!");
    });
    
    // Regenerate Reply (just triggers analysis again)
    regenBtn.addEventListener('click', () => {
        analyzeBtn.click();
    });
});

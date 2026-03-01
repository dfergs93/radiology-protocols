// Chat widget for protocol assistant
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
  ? 'http://localhost:8001'
  : 'https://radiology-protocols.onrender.com';

const CHAT_API = `${API_BASE_URL}/api/chat`;

let chatHistory = [];
let isOpen = false;

// Load chat state from localStorage
function loadChatState() {
  const savedState = localStorage.getItem('protocolChatOpen');
  const savedHistory = localStorage.getItem('protocolChatHistory');

  if (savedState === 'true') {
    isOpen = true;
  }

  if (savedHistory) {
    try {
      chatHistory = JSON.parse(savedHistory);
    } catch (e) {
      chatHistory = [];
    }
  }
}

// Save chat state to localStorage
function saveChatState() {
  localStorage.setItem('protocolChatOpen', isOpen.toString());
  localStorage.setItem('protocolChatHistory', JSON.stringify(chatHistory));
}

function createChatWidget() {
  const widget = document.createElement('div');
  widget.id = 'protocol-chat-widget';
  widget.innerHTML = `
      <button id="chat-toggle" class="chat-toggle" title="Open Protocol Assistant">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
        </svg>
        <span class="chat-badge">AI</span>
      </button>
      
      <div id="chat-panel" class="chat-panel">
        <div class="chat-header">
          <h3>
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display: inline-block; vertical-align: middle; margin-right: 8px;">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
            </svg>
            Protocol Assistant
          </h3>
          <div style="display: flex; gap: 8px;">
            <button id="chat-close" class="chat-close-btn" title="Close">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
            </button>
  
            <button id="chat-clear" class="chat-control-btn" title="Clear history">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="3 6 5 6 21 6"></polyline>
                <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
            </svg>
            </button>
          </div>
        </div>
        
        <div id="chat-messages" class="chat-messages">
          <div class="chat-message assistant">
            <div class="message-content">
              <p><strong>👋 Hi! I'm your radiology protocol assistant.</strong></p>
              <p>Ask me anything about CT protocols, contrast timing, technical parameters, or clinical indications.</p>
              <p style="font-size: 13px; margin-top: 12px; opacity: 0.8;"><strong>Example questions:</strong></p>
              <ul style="font-size: 13px; margin: 4px 0; opacity: 0.8;">
                <li>"What contrast volume for cardiac CTA?"</li>
                <li>"Explain triple phase liver protocol"</li>
                <li>"Compare gated vs non-gated chest CTA"</li>
                <li>"What kV should I use for liver imaging?"</li>
              </ul>
            </div>
          </div>
        </div>
        
        <div class="chat-input-container">
          <textarea 
            id="chat-input" 
            placeholder="Ask about protocols..."
            rows="1"
            autocomplete="off"
          ></textarea>
          <button id="chat-send" title="Send message">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="22" y1="2" x2="11" y2="13"></line>
              <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
            </svg>
          </button>
        </div>
      </div>
    `;

  document.body.appendChild(widget);

  // Toggle listeners
  document.getElementById('chat-toggle').addEventListener('click', openChat);
  document.getElementById('chat-close').addEventListener('click', closeChat);

  // Common listeners
  document.getElementById('chat-send').addEventListener('click', sendMessage);
  document.getElementById('chat-clear').addEventListener('click', clearChatHistory);

  const input = document.getElementById('chat-input');

  // Auto-resize textarea
  input.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 120) + 'px';
  });

  // Send on Enter, new line on Shift+Enter
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  // Restore chat state and history
  loadChatState();
  restoreChatHistory();

  if (isOpen) {
    openChat();
  }
}

function restoreChatHistory() {
  const messagesContainer = document.getElementById('chat-messages');

  // Clear welcome message if we have history
  if (chatHistory.length > 0) {
    messagesContainer.innerHTML = '';
  }

  // Restore previous messages
  chatHistory.forEach(msg => {
    if (msg.role === 'user') {
      addMessage('user', msg.content);
    } else if (msg.role === 'assistant') {
      addMessage('assistant', msg.content, msg.sources);
    }
  });
}

function clearChatHistory() {
  if (confirm('Clear all chat history?')) {
    chatHistory = [];
    saveChatState();

    const messagesContainer = document.getElementById('chat-messages');
    messagesContainer.innerHTML = `
      <div class="chat-message assistant">
        <div class="message-content">
          <p><strong>Chat history cleared!</strong></p>
          <p>Ask me anything about CT protocols.</p>
        </div>
      </div>
    `;
  }
}

function openChat() {
  isOpen = true;

  const panel = document.getElementById('chat-panel');
  const toggle = document.getElementById('chat-toggle');
  const container = document.querySelector('.md-container');

  if (panel) {
    panel.classList.add('open');
  }

  if (container) {
    container.classList.add('chat-open');
  }

  if (toggle) {
    toggle.style.display = 'none';
  }

  const input = document.getElementById('chat-input');
  if (input) {
    input.focus();
  }

  saveChatState();
}

function closeChat() {
  isOpen = false;

  const panel = document.getElementById('chat-panel');
  const toggle = document.getElementById('chat-toggle');
  const container = document.querySelector('.md-container');

  if (panel) {
    panel.classList.remove('open');
  }

  if (container) {
    container.classList.remove('chat-open');
  }

  if (toggle) {
    toggle.style.display = 'flex';
  }

  saveChatState();
}

// NEW: Streaming message handler
async function sendMessage() {
  const input = document.getElementById('chat-input');
  const question = input.value.trim();

  if (!question) return;

  // Disable input while processing
  const sendBtn = document.getElementById('chat-send');
  input.disabled = true;
  sendBtn.disabled = true;

  // Add user message to UI
  addMessage('user', question);
  input.value = '';
  input.style.height = 'auto';

  // Add to history
  chatHistory.push({ role: 'user', content: question });
  saveChatState();

  // Create placeholder for streaming response
  const messageId = `msg-${Date.now()}`;
  const messages = document.getElementById('chat-messages');
  const messageDiv = document.createElement('div');
  messageDiv.id = messageId;
  messageDiv.className = 'chat-message assistant';
  messageDiv.innerHTML = '<div class="message-content"><em>Thinking...</em></div>';
  messages.appendChild(messageDiv);
  messages.scrollTop = messages.scrollHeight;

  let fullResponse = '';
  let sources = [];

  try {
    const currentPage = window.location.pathname;

    const response = await fetch(CHAT_API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        messages: chatHistory,
        current_page: currentPage
      })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
      const { value, done } = await reader.read();
      if (done) break;

      const chunk = decoder.decode(value);
      const lines = chunk.split('\n');

      for (const line of lines) {
        if (line.startsWith('data: ')) {
          try {
            const data = JSON.parse(line.slice(6));

            if (data.sources) {
              // Store sources for later
              sources = data.sources;
            } else if (data.content) {
              // Append content chunk
              fullResponse += data.content;

              // Update message in real-time
              updateStreamingMessage(messageId, fullResponse, sources);
            } else if (data.done) {
              // Streaming complete
              console.log('Streaming complete');
            } else if (data.error) {
              throw new Error(data.error);
            }
          } catch (parseError) {
            console.warn('Failed to parse SSE data:', line, parseError);
          }
        }
      }
    }

    // Save complete response to history
    chatHistory.push({
      role: 'assistant',
      content: fullResponse,
      sources: sources
    });
    saveChatState();

  } catch (error) {
    console.error('Chat error:', error);
    messageDiv.innerHTML = `
      <div class="message-content">
        ❌ Error: ${error.message}
        <br><small>Please check if the backend is running.</small>
      </div>
    `;
  } finally {
    // Re-enable input
    input.disabled = false;
    sendBtn.disabled = false;
    input.focus();
  }
}

// NEW: Update streaming message in real-time
function updateStreamingMessage(messageId, content, sources = []) {
  const messageDiv = document.getElementById(messageId);
  if (!messageDiv) return;

  // Parse markdown to HTML
  let htmlContent;
  if (typeof marked !== 'undefined') {
    marked.setOptions({
      breaks: true,
      gfm: true,
      headerIds: false,
      mangle: false
    });
    htmlContent = marked.parse(content);
  } else {
    htmlContent = content.replace(/\n/g, '<br>');
  }

  let html = `<div class="message-content">${htmlContent}</div>`;

  // Add sources if available
  if (sources && sources.length > 0) {
    html += '<div class="sources"><small><strong>📚 Sources:</strong> ';

    const pathParts = window.location.pathname.split('/').filter(p => p);
    const basePath = pathParts.length > 0 && pathParts[0] !== 'index.html' ? pathParts[0] : '';

    html += sources.map(s => {
      const url = basePath ? `/${basePath}/${s.filepath.replace('.md', '')}` : `/${s.filepath.replace('.md', '')}`;
      return `<a href="${url}" target="_blank">${s.title}</a>`;
    }).join(' • ');

    html += '</small></div>';
  }

  messageDiv.innerHTML = html;

  // Auto-scroll to bottom
  const messagesContainer = document.getElementById('chat-messages');
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function addMessage(role, content, sources = []) {
  const messages = document.getElementById('chat-messages');
  const messageDiv = document.createElement('div');
  const id = `msg-${Date.now()}`;
  messageDiv.id = id;
  messageDiv.className = `chat-message ${role}`;

  // Parse markdown to HTML for assistant messages
  let htmlContent;
  if (role === 'assistant') {
    if (typeof marked !== 'undefined') {
      marked.setOptions({
        breaks: true,
        gfm: true,
        headerIds: false,
        mangle: false
      });
      htmlContent = marked.parse(content);
    } else {
      htmlContent = content.replace(/\n/g, '<br>');
    }
  } else {
    htmlContent = content;
  }

  let html = `<div class="message-content">${htmlContent}</div>`;

  if (sources && sources.length > 0) {
    html += '<div class="sources"><small><strong>📚 Sources:</strong> ';

    const pathParts = window.location.pathname.split('/').filter(p => p);
    const basePath = pathParts.length > 0 && pathParts[0] !== 'index.html' ? pathParts[0] : '';

    html += sources.map(s => {
      const url = basePath ? `/${basePath}/${s.filepath.replace('.md', '')}` : `/${s.filepath.replace('.md', '')}`;
      return `<a href="${url}" target="_blank">${s.title}</a>`;
    }).join(' • ');

    html += '</small></div>';
  }

  messageDiv.innerHTML = html;
  messages.appendChild(messageDiv);
  messages.scrollTop = messages.scrollHeight;

  return id;
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', createChatWidget);
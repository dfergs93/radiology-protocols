// Chat widget for protocol assistant
const CHAT_API = 'http://localhost:8001/api/chat';

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
  
  // Event listeners
  document.getElementById('chat-toggle').addEventListener('click', openChat);
  document.getElementById('chat-close').addEventListener('click', closeChat);
  document.getElementById('chat-send').addEventListener('click', sendMessage);
  document.getElementById('chat-clear').addEventListener('click', clearChatHistory);

  const input = document.getElementById('chat-input');
  
  // Auto-resize textarea
  input.addEventListener('input', function() {
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
      addMessage('assistant', msg.content);
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

async function sendMessage() {
  const input = document.getElementById('chat-input');
  const question = input.value.trim();
  
  if (!question) return;
  
  // Add user message to UI
  addMessage('user', question);
  input.value = '';
  input.style.height = 'auto';
  
  // Add to history
  chatHistory.push({ role: 'user', content: question });
  saveChatState();
  
  // Show typing indicator
  const typingId = addMessage('assistant', '<em>Thinking...</em>');
  
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
      const error = await response.json();
      throw new Error(error.detail || 'API error');
    }
    
    const data = await response.json();
    
    // Remove typing indicator
    document.getElementById(typingId).remove();
    
    // Add assistant response
    addMessage('assistant', data.response, data.sources);
    
    // Add to history
    chatHistory.push({ role: 'assistant', content: data.response });
    saveChatState();
    
  } catch (error) {
    console.error('Chat error:', error);
    document.getElementById(typingId).remove();
    addMessage('assistant', `❌ Error: ${error.message}. Is the backend running?`);
  }
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
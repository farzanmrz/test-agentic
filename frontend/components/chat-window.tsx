import { MessageList } from "@/components/message-list"
import { ChatInput } from "@/components/chat-input"

export function ChatWindow() {
  return (
    <div className="flex h-full flex-col rounded-lg bg-dark-bg-secondary shadow-xl">
      <div className="rounded-t-lg bg-brand-blue px-4 py-3 text-white shadow">
        <h1 className="text-lg font-semibold">Interaction Logs Chat</h1>
      </div>
      <MessageList />
      <ChatInput />
    </div>
  )
}

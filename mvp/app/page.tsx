import { Sidebar } from "@/components/sidebar"
import { MessageList } from "@/components/message-list"
import { ChatInput } from "@/components/chat-input"

export default function DashboardPage() {
  return (
    <div className="flex h-screen w-full bg-dark-bg-primary text-dark-text-primary">
      <Sidebar />
      <main className="relative flex flex-1 flex-col overflow-hidden">
        <MessageList />
        <div className="pointer-events-none absolute bottom-0 left-0 w-full h-48 bg-gradient-to-t from-dark-bg-primary via-dark-bg-primary/80 to-transparent" />
        <div className="absolute bottom-0 left-0 w-full p-4 pb-6 md:px-6 md:pb-8">
          <ChatInput />
        </div>
      </main>
    </div>
  )
}

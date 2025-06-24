"use client"

import React from "react"
import { MessageBubble } from "@/components/message-bubble"

const messages = [
  { id: 1, sender: "user", text: "Hi! Can you help me with the latest interaction logs?" },
  { id: 2, sender: "assistant", text: "I’m pulling the data now." },
  {
    id: 3,
    sender: "assistant",
    text: "It will be ready in a moment. This might be a slightly longer message to test how the text wraps and aligns within the given constraints. Let's see if it behaves as expected.",
  },
  { id: 4, sender: "user", text: "Great, thanks! Also, can you filter by 'urgent' tags?" },
  {
    id: 5,
    sender: "assistant",
    text: "You’re welcome! Yes, I can filter by 'urgent' tags. Applying that filter now...",
  },
  { id: 6, sender: "assistant", text: "Here are the urgent interaction logs from last week." },
]

export function MessageList() {
  const messagesEndRef = React.useRef<HTMLDivElement>(null)

  React.useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [])

  return (
    <div className="flex-1 space-y-6 overflow-y-auto p-4 md:px-6 pb-40">
      <div className="mx-auto max-w-3xl space-y-6">
        {messages.map((message) => (
          <MessageBubble key={message.id} message={message} />
        ))}
      </div>
      <div ref={messagesEndRef} />
    </div>
  )
}

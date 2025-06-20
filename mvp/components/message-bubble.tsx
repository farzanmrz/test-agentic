type Message = {
  id: number
  sender: "user" | "assistant"
  text: string
}

export function MessageBubble({ message }: { message: Message }) {
  if (message.sender === "assistant") {
    return (
      <div className="flex items-start gap-3 pr-10 md:pr-16">
        <div className="w-full text-dark-text-primary">
          <p className="leading-relaxed">{message.text}</p>
        </div>
      </div>
    )
  }

  // User message
  return (
    <div className="flex items-start justify-end gap-3 pl-10 md:pl-16">
      <div className="max-w-xs rounded-lg bg-dark-bg-secondary px-4 py-2.5 text-sm text-dark-text-primary shadow-sm md:max-w-md lg:max-w-xl">
        <p>{message.text}</p>
      </div>
    </div>
  )
}

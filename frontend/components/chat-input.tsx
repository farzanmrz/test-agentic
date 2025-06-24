"use client"

import { useState } from "react"
import { Paperclip, Send } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { cn } from "@/lib/utils"

export function ChatInput() {
  const [message, setMessage] = useState("")
  const hasMessage = message.trim().length > 0

  return (
    <div className="mx-auto w-full max-w-3xl">
      <form
        className="rounded-lg border border-dark-border bg-dark-bg-secondary shadow-lg"
        onSubmit={(e) => {
          e.preventDefault()
          if (!hasMessage) return
          // Handle message sending logic here
          console.log("Sending:", message)
          setMessage("")
        }}
      >
        <Textarea
          placeholder="Type your message here…"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          className="min-h-[112px] w-full resize-none border-0 bg-transparent p-4 shadow-none placeholder:text-dark-text-secondary focus-visible:ring-0 focus-visible:ring-offset-0" // Increased min-h, kept p-4
        />
        <div className="flex items-center justify-between px-3 py-2">
          {" "}
          {/* This div has ~48px height */}
          <Button
            variant="ghost"
            size="icon"
            className="shrink-0 text-dark-text-secondary hover:text-dark-text-primary"
          >
            <Paperclip className="h-5 w-5" />
            <span className="sr-only">Attach file</span>
          </Button>
          <Button
            type="submit"
            size="icon"
            disabled={!hasMessage}
            className={cn(
              "shrink-0 rounded-full w-8 h-8 flex items-center justify-center transition-colors", // h-8 for button
              hasMessage
                ? "bg-dark-text-primary text-dark-bg-secondary"
                : "bg-dark-bg-tertiary text-dark-text-secondary cursor-not-allowed",
            )}
          >
            <Send className="h-5 w-5" />
            <span className="sr-only">Send message</span>
          </Button>
        </div>
      </form>
      <p className="mt-2 text-center text-xs text-dark-text-secondary">
        Optium can make mistakes. Please double check the outputs.
      </p>
    </div>
  )
}

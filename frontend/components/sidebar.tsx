"use client"
import { useState } from "react"
import { Icons } from "@/components/icons"
import { cn } from "@/lib/utils"

const sidebarNav = [
  { type: "header", title: "Admin" },
  { type: "link", title: "Board Minutes", href: "#" },
  { type: "header", title: "Sales" },
  { type: "link", title: "Targets", href: "#" },
  { type: "link", title: "CRM Reports", href: "#" },
  { type: "link", title: "Interaction Logs", href: "#" },
  { type: "header", title: "Manufacturing" },
  { type: "link", title: "Production Report", href: "#" },
  { type: "link", title: "Quality Report", href: "#" },
]

export function Sidebar() {
  // Set default active to "Board Minutes"
  const [activeTitle, setActiveTitle] = useState("Board Minutes")

  return (
    <aside className="hidden md:flex w-64 flex-col bg-black">
      <div className="flex h-16 items-center px-4">
        <Icons.logo className="h-6 w-6 text-brand-blue" />
      </div>
      <nav className="flex-1 space-y-1 overflow-y-auto px-2 pb-4">
        {sidebarNav.map((item, index) => {
          if (item.type === "header") {
            return (
              <div key={index} className="px-2 pt-6 pb-2 text-sm font-medium text-dark-text-secondary tracking-wider">
                {item.title}
              </div>
            )
          }
          return (
            <a
              key={index}
              href={item.href}
              onClick={e => {
                e.preventDefault()
                setActiveTitle(item.title)
              }}
              className={cn(
                "flex items-center rounded-md py-2 px-2 text-sm font-medium transition-colors",
                activeTitle === item.title
                  ? "bg-dark-bg-secondary text-dark-text-primary"
                  : "text-dark-text-primary hover:bg-dark-bg-secondary hover:text-dark-text-primary",
              )}
            >
              {item.title}
            </a>
          )
        })}
      </nav>
    </aside>
  )
}

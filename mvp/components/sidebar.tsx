"use client"
import { Icons } from "@/components/icons"
import { cn } from "@/lib/utils"

const sidebarNav = [
  { type: "header", title: "Sales" }, // Changed to "Sales"
  { type: "link", title: "Targets", href: "#" },
  { type: "link", title: "CRM Reports", href: "#" },
  { type: "link", title: "Interaction Logs", href: "#", active: true },
  { type: "header", title: "Manufacturing" }, // Changed to "Manufacturing"
  { type: "link", title: "Production Report", href: "#" },
  { type: "link", title: "Quality Report", href: "#" },
]

export function Sidebar() {
  return (
    <aside className="hidden md:flex w-64 flex-col bg-black">
      <div className="flex h-16 items-center px-4">
        {" "}
        {/* Removed gap, Optium text */}
        <Icons.logo className="h-6 w-6 text-brand-blue" /> {/* Reduced logo size */}
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
              className={cn(
                "flex items-center rounded-md py-2 px-2 text-sm font-medium transition-colors",
                item.active
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

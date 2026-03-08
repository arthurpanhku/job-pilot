import { Home, Briefcase, MessageSquare, User, Settings, PieChart, Clock, Lightbulb } from "lucide-react"
import { cn } from "@/lib/utils"
import Image from "next/image"

interface SidebarProps {
    className?: string
}

export function Sidebar({ className }: SidebarProps) {
    const navItems = [
        { icon: Home, label: "Home", active: false },
        { icon: MessageSquare, label: "Messages", active: false },
        { icon: Briefcase, label: "Platform", active: false },
        { icon: PieChart, label: "Matches", active: false },
        { icon: Briefcase, label: "JobPilot", active: true },
        { icon: Clock, label: "Previous", active: false },
        { icon: Lightbulb, label: "Advice", active: false },
    ]

    return (
        <div className={cn("w-64 bg-slate-950 text-slate-400 flex flex-col h-screen border-r border-slate-800", className)}>
            <div className="p-6">
                <div className="flex items-center gap-3 text-white text-xl font-bold">
                    <div className="relative h-10 w-10 overflow-hidden rounded-lg">
                        <Image
                            src="/logo.jpg"
                            alt="JobPilot Logo"
                            fill
                            className="object-cover"
                        />
                    </div>
                    JobPilot
                </div>
            </div>

            <nav className="flex-1 px-4 space-y-2 mt-4">
                <div className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-4 px-2">
                    Menu
                </div>
                {navItems.map((item) => (
                    <button
                        key={item.label}
                        className={cn(
                            "w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors",
                            item.active
                                ? "bg-slate-800 text-white shadow-sm"
                                : "hover:bg-slate-900 hover:text-slate-200"
                        )}
                    >
                        <item.icon className={cn("h-5 w-5", item.active ? "text-blue-400" : "text-slate-500")} />
                        {item.label}
                    </button>
                ))}
            </nav>

            <div className="p-4 mt-auto border-t border-slate-800">
                <button className="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium hover:bg-slate-900 hover:text-slate-200 transition-colors">
                    <Settings className="h-5 w-5 text-slate-500" />
                    Settings
                </button>
                <div className="mt-4 flex items-center gap-3 px-3">
                    <div className="h-8 w-8 rounded-full bg-slate-700 flex items-center justify-center text-xs text-white">
                        VP
                    </div>
                    <div className="text-sm">
                        <div className="text-white font-medium">User Profile</div>
                        <div className="text-xs text-slate-500">View Profile</div>
                    </div>
                </div>
            </div>
        </div>
    )
}

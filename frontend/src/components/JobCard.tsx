import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"
import { MoreHorizontal } from "lucide-react"

interface JobCardProps {
    company: string
    title: string
    type: string
    location: string
    logoColor: string
    logoText: string
    status: "apply" | "save"
    verified?: boolean
}

export function JobCard({ company, title, type, location, logoColor, logoText, status, verified }: JobCardProps) {
    return (
        <div className="bg-slate-900/50 hover:bg-slate-900 border border-slate-800 rounded-xl p-4 flex items-center justify-between transition-colors group">
            <div className="flex items-center gap-4">
                {/* Company Logo */}
                <div className={cn("h-12 w-12 rounded-xl flex items-center justify-center text-white font-bold text-lg", logoColor)}>
                    {logoText}
                </div>

                {/* Job Details */}
                <div>
                    <div className="flex items-center gap-2 mb-1">
                        <span className="text-sm font-medium text-white">{company}</span>
                        {verified && (
                            <span className="bg-blue-500/20 text-blue-400 p-0.5 rounded">
                                <svg className="h-3 w-3" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z" /></svg>
                            </span>
                        )}
                    </div>
                    <h3 className="text-lg font-semibold text-white mb-1">{title}</h3>
                    <div className="flex items-center gap-2 text-sm text-slate-400">
                        <span>{type}</span>
                        <span className="h-1 w-1 rounded-full bg-slate-600"></span>
                        <span className="flex items-center gap-1">
                            <svg className="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                            </svg>
                            {location}
                        </span>
                    </div>
                </div>
            </div>

            {/* Actions */}
            <div className="flex items-center gap-3">
                {status === "apply" ? (
                    <Button className="bg-white text-black hover:bg-slate-200 font-semibold px-6">
                        Apply Now
                    </Button>
                ) : (
                    <Button variant="outline" className="bg-slate-800 border-slate-700 text-white hover:bg-slate-700 hover:text-white px-6">
                        Save Job
                    </Button>
                )}
                <button className="p-2 text-slate-500 hover:text-white transition-colors">
                    <MoreHorizontal className="h-5 w-5" />
                </button>
            </div>
        </div>
    )
}

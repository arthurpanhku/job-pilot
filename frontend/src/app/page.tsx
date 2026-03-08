import { Sidebar } from "@/components/Sidebar"
import { JobCard } from "@/components/JobCard"
import { Bell, Search, User } from "lucide-react"

export default function Home() {
  const jobs = [
    {
      company: "Company",
      title: "Senior Software Engineer",
      type: "Full-time",
      location: "San Francisco, CA",
      logoColor: "bg-purple-600",
      logoText: "L",
      status: "apply" as const,
      verified: true
    },
    {
      company: "Company",
      title: "Product Manager",
      type: "Full-time",
      location: "San Francisco, CA",
      logoColor: "bg-green-500",
      logoText: "M",
      status: "apply" as const,
      verified: true
    },
    {
      company: "Company",
      title: "Product Manager",
      type: "Remote",
      location: "New York, NY",
      logoColor: "bg-red-500",
      logoText: "X",
      status: "save" as const,
      verified: true
    },
    {
      company: "Compar",
      title: "Product Names CanIE In Nundtt",
      type: "Full-time",
      location: "New York, NY",
      logoColor: "bg-orange-500",
      logoText: "N",
      status: "save" as const
    },
    {
      company: "Ampany",
      title: "Product Manager Bin",
      type: "Contract",
      location: "San Francisco, CA",
      logoColor: "bg-blue-600",
      logoText: "A",
      status: "save" as const,
      verified: true
    },
    {
      company: "Dantor",
      title: "Product Manager",
      type: "Full-time",
      location: "New York, NY",
      logoColor: "bg-blue-400",
      logoText: "S",
      status: "save" as const,
      verified: true
    }
  ]

  return (
    <div className="flex min-h-screen bg-black font-sans">
      <Sidebar />

      <main className="flex-1 overflow-auto">
        <div className="p-8 max-w-6xl mx-auto">
          {/* Header */}
          <header className="flex items-center justify-between mb-8">
            <h1 className="text-2xl font-bold text-white">Home</h1>

            <div className="flex-1 max-w-md mx-8 relative">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-slate-500" />
              <input
                type="text"
                placeholder="Search Jobs"
                className="w-full bg-slate-900 border-none rounded-lg pl-10 pr-4 py-2.5 text-white placeholder:text-slate-500 focus:ring-1 focus:ring-slate-700"
              />
            </div>

            <div className="flex items-center gap-4">
              <button className="relative p-2 text-slate-400 hover:text-white transition-colors">
                <Bell className="h-6 w-6" />
                <span className="absolute top-2 right-2 h-2 w-2 bg-red-500 rounded-full border-2 border-black"></span>
              </button>
              <div className="h-8 w-8 rounded-full bg-slate-800 flex items-center justify-center overflow-hidden border border-slate-700">
                <User className="h-5 w-5 text-slate-400" />
              </div>
            </div>
          </header>

          {/* Section Title */}
          <div className="mb-6">
            <h2 className="text-xl font-bold text-white mb-4">Job Listings</h2>

            <div className="space-y-3">
              {jobs.map((job, i) => (
                <JobCard key={i} {...job} />
              ))}
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}

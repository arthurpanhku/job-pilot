import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center p-8 bg-slate-50">
      <header className="w-full max-w-5xl mb-8 flex justify-between items-center">
        <h1 className="text-3xl font-bold tracking-tight text-slate-900">JobPilot Dashboard</h1>
        <div className="flex gap-2">
          <span className="px-3 py-1 bg-yellow-100 text-yellow-800 rounded-full text-sm font-medium border border-yellow-200">
            ⚠ Risk Level: Low (Stealth Mode)
          </span>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full max-w-5xl">
        {/* Job Search Section */}
        <Card className="col-span-1">
          <CardHeader>
            <CardTitle>Job Search</CardTitle>
            <CardDescription>Find jobs on LinkedIn and Indeed</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid gap-2">
              <label className="text-sm font-medium">Keywords</label>
              <input
                type="text"
                placeholder="Software Engineer, React..."
                className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
              />
            </div>
            <div className="grid gap-2">
              <label className="text-sm font-medium">Location</label>
              <input
                type="text"
                placeholder="Remote, San Francisco..."
                className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
              />
            </div>
            <div className="flex items-center gap-2 mt-2">
              <input type="checkbox" id="stealth" className="h-4 w-4 rounded border-gray-300 text-primary focus:ring-primary" defaultChecked />
              <label htmlFor="stealth" className="text-sm text-gray-600">Enable Stealth Mode (Anti-detection)</label>
            </div>
          </CardContent>
          <CardFooter className="flex justify-between">
            <Button variant="outline">Clear</Button>
            <Button>Search Jobs</Button>
          </CardFooter>
        </Card>

        {/* Status / Control Panel */}
        <Card className="col-span-1">
          <CardHeader>
            <CardTitle>Automation Status</CardTitle>
            <CardDescription>Monitor active bots and applications</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex justify-between items-center p-3 bg-white border rounded-lg shadow-sm">
                <div className="flex items-center gap-3">
                  <div className="h-2 w-2 rounded-full bg-green-500"></div>
                  <span className="font-medium">Backend Service</span>
                </div>
                <span className="text-sm text-green-600 bg-green-50 px-2 py-1 rounded">Online</span>
              </div>

              <div className="flex justify-between items-center p-3 bg-white border rounded-lg shadow-sm">
                <div className="flex items-center gap-3">
                  <div className="h-2 w-2 rounded-full bg-gray-300"></div>
                  <span className="font-medium">Active Applications</span>
                </div>
                <span className="text-sm text-gray-500">0 Running</span>
              </div>

              <div className="p-4 bg-blue-50 border border-blue-100 rounded-lg text-sm text-blue-800">
                <p className="font-semibold mb-1">ℹ Safe Mode Active</p>
                Applications will pause before submission for manual review. Screenshots will be saved to verify forms.
              </div>
            </div>
          </CardContent>
          <CardFooter>
            <Button variant="secondary" className="w-full">View Logs</Button>
          </CardFooter>
        </Card>

        {/* Recent Applications (Full Width) */}
        <Card className="col-span-1 md:col-span-2">
          <CardHeader>
            <CardTitle>Recent Applications</CardTitle>
            <CardDescription>History of automated applications</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="rounded-md border">
              <div className="relative w-full overflow-auto">
                <table className="w-full caption-bottom text-sm">
                  <thead className="[&_tr]:border-b">
                    <tr className="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted">
                      <th className="h-12 px-4 text-left align-middle font-medium text-muted-foreground">Job Title</th>
                      <th className="h-12 px-4 text-left align-middle font-medium text-muted-foreground">Company</th>
                      <th className="h-12 px-4 text-left align-middle font-medium text-muted-foreground">Platform</th>
                      <th className="h-12 px-4 text-left align-middle font-medium text-muted-foreground">Status</th>
                      <th className="h-12 px-4 text-right align-middle font-medium text-muted-foreground">Action</th>
                    </tr>
                  </thead>
                  <tbody className="[&_tr:last-child]:border-0">
                    <tr className="border-b transition-colors hover:bg-muted/50">
                      <td className="p-4 align-middle font-medium">Senior Frontend Engineer</td>
                      <td className="p-4 align-middle">TechCorp Inc.</td>
                      <td className="p-4 align-middle">LinkedIn</td>
                      <td className="p-4 align-middle"><span className="inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 border-transparent bg-yellow-100 text-yellow-800 hover:bg-yellow-200">Pending Review</span></td>
                      <td className="p-4 align-middle text-right"><Button size="sm" variant="outline">Review</Button></td>
                    </tr>
                    <tr className="border-b transition-colors hover:bg-muted/50">
                      <td className="p-4 align-middle font-medium">Python Developer</td>
                      <td className="p-4 align-middle">DataSystems</td>
                      <td className="p-4 align-middle">Indeed</td>
                      <td className="p-4 align-middle"><span className="inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 border-transparent bg-green-100 text-green-800 hover:bg-green-200">Applied</span></td>
                      <td className="p-4 align-middle text-right"><Button size="sm" variant="ghost">Details</Button></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </main>
  )
}

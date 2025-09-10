import React, {useMemo, useState} from "react";

// Simple, static UI mock for your deck. Screenshot this and drop it into the slide.
// Tailwind only; no external data calls. Minimal, clean, high-contrast.

const sample = {
  sprint: "Sprint 28",
  range: "Aug 25–29",
  team: "Sherlock QA",
  stats: {
    timeSaved: "2.6h / lead / wk",
    extraction: "93% extraction accuracy",
    correlation: ">0.82 corr. vs lead ratings"
  },
  people: [
    {
      id: 1,
      name: "Nabil A.",
      role: "SDET",
      score: 86,
      trend: [70, 78, 83, 86],
      badges: ["Automation +1", "0 reopens"],
      why: {
        completion: "6/6 critical tests executed",
        complexity: "+34 complexity points (deep integration cases)",
        quality: "0 defects reopened, 1 blocker cleared",
        impact: "+1 automation script, +6% coverage",
        timeliness: "All on-time; 1 ad-hoc validation"
      },
      evidence: [
        {label: "Jira QAX-342", url: "#"},
        {label: "TestRail Run 827", url: "#"}
      ]
    },
    {
      id: 2,
      name: "Amin A.",
      role: "SeSDET",
      score: 81,
      trend: [69, 74, 78, 81],
      badges: ["Blocker resolved"],
      why: {
        completion: "14 manual TCs, 3 exploratory",
        complexity: "+22 complexity points",
        quality: "1 minor defect, 0 reopens",
        impact: "+2% module coverage",
        timeliness: "On-time; supported release smoke"
      },
      evidence: [
        {label: "Jira BUG-1102", url: "#"}
      ]
    },
    {
      id: 3,
      name: "Riyad A.",
      role: "QA Analyssst",
      score: 76,
      trend: [72, 74, 75, 76],
      badges: ["Stabilized flaky"],
      why: {
        completion: "3 regression batches",
        complexity: "+18 complexity points",
        quality: "1 flaky test fixed",
        impact: "Stability +",
        timeliness: "On-time"
      },
      evidence: []
    }
  ]
};

function Sparkline({points}:{points:number[]}){
  // crude sparkline using inline SVG
  const max = Math.max(...points);
  const min = Math.min(...points);
  const norm = points.map((p,i)=>({x: i*(100/(points.length-1)), y: 20 - ((p-min)/(max-min||1))*20 }));
  const d = ["M", norm[0].x, norm[0].y, ...norm.slice(1).flatMap(p=>["L", p.x, p.y])].join(" ");
  return (
    <svg viewBox="0 0 100 20" className="w-24 h-5">
      <path d={d} fill="none" stroke="currentColor" strokeWidth="2" />
    </svg>
  );
}

export default function DashboardMock(){
  const [selected, setSelected] = useState(sample.people[0].id);
  const person = useMemo(()=> sample.people.find(p=>p.id===selected)!, [selected]);
  return (
    <div className="min-h-screen w-full bg-white text-slate-900">
      {/* Header */}
      <div className="bg-gradient-to-r from-fuchsia-600 to-blue-600 text-white py-6 px-8 flex items-center justify-between shadow">
        <div>
          <div className="text-xs uppercase tracking-wider opacity-90">Performance Evaluator — {sample.team}</div>
          <h1 className="text-2xl font-bold">{sample.sprint} <span className="font-medium opacity-90">({sample.range})</span></h1>
        </div>
        <div className="flex gap-6 text-sm">
          <div className="bg-white/15 rounded-xl px-4 py-2">
            <div className="opacity-90">Time saved</div>
            <div className="font-semibold">{sample.stats.timeSaved}</div>
          </div>
          <div className="bg-white/15 rounded-xl px-4 py-2">
            <div className="opacity-90">Extraction</div>
            <div className="font-semibold">{sample.stats.extraction}</div>
          </div>
          <div className="bg-white/15 rounded-xl px-4 py-2">
            <div className="opacity-90">Agreement</div>
            <div className="font-semibold">{sample.stats.correlation}</div>
          </div>
        </div>
      </div>

      {/* Filters */}
      <div className="px-8 py-4 grid grid-cols-3 gap-4 border-b">
        <div>
          <label className="text-xs uppercase tracking-wide text-slate-500">Team</label>
          <div className="mt-1 border rounded-xl px-3 py-2">{sample.team}</div>
        </div>
        <div>
          <label className="text-xs uppercase tracking-wide text-slate-500">Role</label>
          <div className="mt-1 border rounded-xl px-3 py-2">SDET / QA</div>
        </div>
        <div>
          <label className="text-xs uppercase tracking-wide text-slate-500">Date Range</label>
          <div className="mt-1 border rounded-xl px-3 py-2">{sample.range}</div>
        </div>
      </div>

      {/* Main content */}
      <div className="px-8 py-6 grid grid-cols-12 gap-6">
        {/* Leaderboard */}
        <div className="col-span-7">
          <h2 className="text-lg font-semibold mb-3">Top Contributors</h2>
          <div className="space-y-3">
            {sample.people.map(p=> (
              <button key={p.id} onClick={()=>setSelected(p.id)} className={`w-full text-left border rounded-2xl p-4 hover:shadow transition ${selected===p.id?"ring-2 ring-fuchsia-500":""}`}>
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <div className="w-9 h-9 rounded-full bg-gradient-to-br from-fuchsia-500 to-blue-500 text-white flex items-center justify-center font-semibold">{p.name.split(" ")[0][0]}</div>
                    <div>
                      <div className="font-medium">{p.name} <span className="text-slate-500 text-sm">• {p.role}</span></div>
                      <div className="flex gap-2 text-xs mt-1 text-slate-600">
                        {p.badges.map(b=> <span key={b} className="border rounded-full px-2 py-[2px]">{b}</span>)}
                      </div>
                    </div>
                  </div>
                  <div className="flex items-center gap-4">
                    <div className="text-sm text-slate-500">Score</div>
                    <div className="text-2xl font-bold tabular-nums">{p.score}</div>
                    <div className="text-slate-500"><Sparkline points={p.trend} /></div>
                  </div>
                </div>
              </button>
            ))}
          </div>
        </div>

        {/* Why panel */}
        <div className="col-span-5">
          <h2 className="text-lg font-semibold mb-3">Why this score</h2>
          <div className="border rounded-2xl p-5 space-y-3">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-fuchsia-500 to-blue-500" />
              <div>
                <div className="font-semibold">{person.name} <span className="text-slate-500 font-normal">• {person.role}</span></div>
                <div className="text-slate-500 text-sm">Score <span className="font-semibold text-slate-700">{person.score}</span></div>
              </div>
            </div>
            <ul className="text-sm leading-6 text-slate-700 list-disc list-inside">
              <li><span className="font-medium">Completion:</span> {person.why.completion}</li>
              <li><span className="font-medium">Complexity:</span> {person.why.complexity}</li>
              <li><span className="font-medium">Quality:</span> {person.why.quality}</li>
              <li><span className="font-medium">Impact:</span> {person.why.impact}</li>
              <li><span className="font-medium">Timeliness:</span> {person.why.timeliness}</li>
            </ul>
            <div className="text-xs text-slate-500">Evidence:
              <div className="mt-1 flex flex-wrap gap-2">
                {person.evidence.length? person.evidence.map(e=> (
                  <span key={e.label} className="border rounded-full px-2 py-1">{e.label}</span>
                )): <span className="italic">—</span>}
              </div>
            </div>
            <div className="pt-3 border-t text-xs text-slate-500">
              Formula (role‑tuned): 0.35·Progress + 0.25·Complexity + 0.20·Quality + 0.10·Impact + 0.10·Timeliness
            </div>
          </div>
        </div>
      </div>

      {/* Footer note */}
      <div className="px-8 pb-8 text-xs text-slate-500">Privacy‑first, runs inside tenant • Confidence + human override • Audit log</div>
    </div>
  );
}

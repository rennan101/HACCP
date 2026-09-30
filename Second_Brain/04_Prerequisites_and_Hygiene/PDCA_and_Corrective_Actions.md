# Corrective Actions & The PDCA Cycle

## Overview
When a [[7_HACCP_Principles|Critical Limit]] is breached at any [[HTST_Pasteurisation|Critical Control Point]], immediate corrective action is mandatory to restore process control, quarantine suspect product, and prevent recurrence.

---

## The PDCA Continuous Improvement Cycle

```mermaid
flowchart TD
    P["1. PLAN<br/>• Conduct Hazard Analysis<br/>• Establish Critical Limits & SOPs"] --> D["2. DO<br/>• Execute HACCP Controls<br/>• Real-time CCP Monitoring"]
    D --> C["3. CHECK<br/>• Audit Daily Shift Logs<br/>• Calibrate Probes & Review Lab KPIs"]
    C --> A["4. ACT<br/>• Investigate NCR Deviations<br/>• Standardise Fixes & Update Plan"]
    A --> P
```

---

## The 4-Step Corrective Action Workflow
1. **Immediate Line Containment**: Trigger automated flow divert valves or stop packaging conveyors immediately.
2. **Quarantine & Tagging**: Apply physical Yellow/Red **ON-HOLD** tags to affected pallets and lock lot numbers in ERP.
3. **Root Cause Analysis (RCA)**: Engineering and QA investigate the underlying failure (e.g., steam valve, seal failure).
4. **Disposition & Record**: Suspect product is either re-pasteurised, downgraded, or destroyed upon Quality Manager sign-off.

---

## Related Notes
- [[7_HACCP_Principles]]
- [[HTST_Pasteurisation]]
- [[Microbiological_KPIs_Dairy]]
- [[Regulation_EC_852_2004_and_EHO]]
- [[HACCP_Master_Index]]

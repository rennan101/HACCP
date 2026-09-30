import json
import os

SLIDES_CONFIG = [
    {
        "slide_num": 1,
        "layout_mode": "split_photo",
        "title": "Welcome & Course Overview",
        "category": "HACCP Level 2 Training",
        "subtitle": "Essential food safety management standards tailored for food and dairy processing",
        "audio_file": "assets/audio/Slide_01_Welcome_Course_Title.mp3",
        "image_file": "assets/images/slide_01.jpg",
        "elements": [
            {
                "id": "s1_card1",
                "start_time": 4.5,
                "end_time": 14.5,
                "tag": "Statutory Standard",
                "heading": "UK & EU Regulation (EC) No 852/2004",
                "description": "Mandatory hygiene framework ensuring safety from raw milk intake to packaged consumer goods.",
                "color": "primary"
            },
            {
                "id": "s1_card2",
                "start_time": 14.5,
                "end_time": 25.0,
                "tag": "Operational Scope",
                "heading": "Comprehensive Plant Protection",
                "description": "Applies across intake decks, pasteurisation bays, cheese vats, packaging lines and QA labs.",
                "color": "success"
            },
            {
                "id": "s1_banner",
                "start_time": 25.0,
                "end_time": 35.0,
                "type": "banner",
                "heading": "Let's Get Started with HACCP Excellence",
                "description": "Protecting our consumers, our brand, and everyday food safety.",
                "color": "accent"
            }
        ]
    },
    {
        "slide_num": 2,
        "layout_mode": "full_width_grid_2col",
        "title": "Course Aim & Learning Syllabus",
        "category": "Course Agenda",
        "subtitle": "Comprehensive syllabus and core learning outcomes for dairy professionals",
        "audio_file": "assets/audio/Slide_02_Course_Aim_Learning_Agenda.mp3",
        "elements": [
            {"id": "s2_t1", "start_time": 6.5, "end_time": 12.0, "tag": "Module 1", "heading": "1. What is HACCP & History", "description": "From NASA space missions to modern food legislation."},
            {"id": "s2_t2", "start_time": 12.0, "end_time": 17.5, "tag": "Module 2", "heading": "2. Food Safety Hazards", "description": "Biological, chemical, physical, and allergen risk factors."},
            {"id": "s2_t3", "start_time": 17.5, "end_time": 23.0, "tag": "Module 3", "heading": "3. Legislation & Codex", "description": "UK statutory compliance and Codex Alimentarius guidelines."},
            {"id": "s2_t4", "start_time": 23.0, "end_time": 29.0, "tag": "Module 4", "heading": "4. The 7 Principles", "description": "Foundational methodology for systematic hazard control."},
            {"id": "s2_t5", "start_time": 29.0, "end_time": 34.5, "tag": "Module 5", "heading": "5. Determining CCPs", "description": "Structured decision tree methodology and parameter limits."},
            {"id": "s2_t6", "start_time": 34.5, "end_time": 41.0, "tag": "Module 6", "heading": "6. Dairy CCPs & PRPs", "description": "Filtration, pasteurisation, chilling, metal detection & PRPs."},
            {"id": "s2_t7", "start_time": 41.0, "end_time": 50.0, "tag": "Module 7", "heading": "7. PDCA Cycle & Assessment", "description": "Continuous improvement, personal liability, and 10-question evaluation."}
        ]
    },
    {
        "slide_num": 3,
        "layout_mode": "comparison_split",
        "title": "What is HACCP?",
        "category": "Core Definition",
        "subtitle": "Hazard Analysis Critical Control Point: built-in prevention at source",
        "audio_file": "assets/audio/Slide_03_What_is_HACCP.mp3",
        "elements": [
            {
                "id": "s3_comp_old",
                "start_time": 13.0,
                "end_time": 26.0,
                "type": "comparison_old",
                "tag": "Traditional Approach",
                "heading": "End-Product Inspection",
                "description": "• Testing finished product after manufacture\n• High recall risk: unsafe product is already packaged\n• Impossible to test 100% of manufactured units\n• Delayed discovery causes massive food waste",
                "color": "danger"
            },
            {
                "id": "s3_comp_new",
                "start_time": 26.0,
                "end_time": 42.0,
                "type": "comparison_new",
                "tag": "HACCP Modern Standard",
                "heading": "Process Control at Source",
                "description": "• Identifies and controls hazards at each stage\n• Continuous real-time monitoring of critical limits\n• Immediate automated divert & correction\n• Prevents, reduces or eliminates risks proactively",
                "color": "success"
            },
            {
                "id": "s3_banner",
                "start_time": 42.0,
                "end_time": 52.0,
                "type": "banner",
                "heading": "Built Upon 7 Fundamental Codex Principles",
                "description": "Guarantees end-to-end safety from raw milk intake to final packaged goods.",
                "color": "accent"
            }
        ]
    },
    {
        "slide_num": 4,
        "layout_mode": "horizontal_timeline",
        "title": "Where Does HACCP Come From?",
        "category": "Historical Origins",
        "subtitle": "From 1960s NASA space missions to statutory international food legislation",
        "audio_file": "assets/audio/Slide_04_Where_Does_HACCP_Come_From.mp3",
        "elements": [
            {"id": "s4_era1", "start_time": 2.0, "end_time": 17.0, "tag": "1960s", "heading": "NASA & Pillsbury", "description": "Developed 100% safe, pathogen-free food for astronauts in zero gravity."},
            {"id": "s4_era2", "start_time": 17.0, "end_time": 28.0, "tag": "1970s", "heading": "US FDA Adoption", "description": "Formalised principles for commercial canning to stop botulism outbreaks."},
            {"id": "s4_era3", "start_time": 28.0, "end_time": 38.0, "tag": "1990s", "heading": "Codex Standard", "description": "FAO / WHO international benchmark adopted HACCP worldwide."},
            {"id": "s4_era4", "start_time": 38.0, "end_time": 52.0, "tag": "2000s - Present", "heading": "Mandatory UK Law", "description": "Regulation (EC) 852/2004 makes HACCP compulsory for all food plants."}
        ]
    },
    {
        "slide_num": 5,
        "layout_mode": "split_photo",
        "title": "What Are the Hazards in Food?",
        "category": "Hazard Identification",
        "subtitle": "The four fundamental categories of food safety hazards in dairy processing",
        "audio_file": "assets/audio/Slide_05_What_Are_the_Hazards_in_Food.mp3",
        "image_file": "assets/images/slide_05.jpg",
        "elements": [
            {"id": "s5_h1", "start_time": 7.0, "end_time": 19.0, "tag": "Biological", "heading": "1. Biological Hazards", "description": "Listeria monocytogenes, Salmonella, pathogenic E. coli and Bacillus cereus spores.", "color": "danger"},
            {"id": "s5_h2", "start_time": 19.0, "end_time": 30.0, "tag": "Chemical", "heading": "2. Chemical Hazards", "description": "Detergent residues, CIP chemicals, sanitisers, and machinery lubricants.", "color": "warning"},
            {"id": "s5_h3", "start_time": 30.0, "end_time": 42.0, "tag": "Physical", "heading": "3. Physical Hazards", "description": "Glass fragments, brittle hard plastics, metal swarf, hair, screws, and pests.", "color": "primary"},
            {"id": "s5_h4", "start_time": 42.0, "end_time": 55.0, "tag": "Allergen", "heading": "4. Allergen Hazards", "description": "Unintended cross-contact with any of the 14 statutory recognized allergens.", "color": "purple"}
        ]
    },
    {
        "slide_num": 6,
        "layout_mode": "full_width_alert_split",
        "title": "Regulations & Legal Framework",
        "category": "Statutory Compliance",
        "subtitle": "Codex Alimentarius baseline, Regulation (EC) 852/2004 and EHO enforcement",
        "audio_file": "assets/audio/Slide_06_Regulations_and_Guidelines.mp3",
        "elements": [
            {"id": "s6_c1", "start_time": 2.0, "end_time": 15.0, "tag": "International Benchmark", "heading": "Codex Alimentarius (FAO / WHO)", "description": "Defines what hygiene rules are required internationally to protect global food trade."},
            {"id": "s6_c2", "start_time": 15.0, "end_time": 30.0, "tag": "Statutory Law", "heading": "Regulation (EC) No 852/2004", "description": "Mandatory UK legislation requiring all food businesses to put in place a permanent HACCP system."},
            {"id": "s6_c3", "start_time": 30.0, "end_time": 52.0, "type": "warning_box", "tag": "Enforcement Authority", "heading": "Environmental Health Officer (EHO) Powers", "description": "EHOs inspect food plants regularly. Failure to maintain HACCP can result in immediate site closure, heavy statutory fines, and criminal prosecution.", "color": "danger"}
        ]
    },
    {
        "slide_num": 7,
        "layout_mode": "full_width_grid_2col",
        "title": "The 7 Principles of HACCP",
        "category": "Codex Methodology",
        "subtitle": "The complete seven-step framework for dairy safety management",
        "audio_file": "assets/audio/Slide_07_The_7_HACCP_Principles.mp3",
        "elements": [
            {"id": "s7_p1", "start_time": 2.0, "end_time": 10.0, "tag": "Principle 1", "heading": "1. Conduct Hazard Analysis", "description": "Identify all biological, chemical, physical, and allergen risks across the process."},
            {"id": "s7_p2", "start_time": 10.0, "end_time": 20.0, "tag": "Principle 2", "heading": "2. Determine CCPs", "description": "Identify steps essential to prevent, eliminate, or reduce hazards to safe levels."},
            {"id": "s7_p3", "start_time": 20.0, "end_time": 30.0, "tag": "Principle 3", "heading": "3. Establish Critical Limits", "description": "Define clear pass/fail safety boundaries (e.g. >72°C / 15s in pasteurisation)."},
            {"id": "s7_p4", "start_time": 30.0, "end_time": 40.0, "tag": "Principle 4", "heading": "4. Establish Monitoring", "description": "Continuous real-time tracking and logging of all critical control parameters."},
            {"id": "s7_p5", "start_time": 40.0, "end_time": 50.0, "tag": "Principle 5", "heading": "5. Corrective Actions", "description": "Pre-planned immediate procedures when monitoring shows a loss of control."},
            {"id": "s7_p6", "start_time": 50.0, "end_time": 60.0, "tag": "Principle 6", "heading": "6. Verification Procedures", "description": "Audits, probe calibrations, and laboratory testing to confirm the system works."},
            {"id": "s7_p7", "start_time": 60.0, "end_time": 76.0, "tag": "Principle 7", "heading": "7. Documented Records", "description": "Maintain robust documentation, trace logs, and due diligence compliance records."}
        ]
    },
    {
        "slide_num": 8,
        "layout_mode": "horizontal_flow",
        "title": "Determining Critical Control Points",
        "category": "CCP Methodology",
        "subtitle": "Structured decision tree methodology to establish control points",
        "audio_file": "assets/audio/Slide_08_Determine_Critical_Control_Points_CCPs.mp3",
        "elements": [
            {"id": "s8_s1", "start_time": 2.0, "end_time": 14.0, "tag": "Step 1", "heading": "Process Flow Diagram", "description": "Construct an accurate flow diagram mapping every stage from raw milk intake to final shipping."},
            {"id": "s8_s2", "start_time": 14.0, "end_time": 27.0, "tag": "Step 2", "heading": "Hazard Analysis", "description": "Evaluate the likelihood and severity of potential hazards at each step."},
            {"id": "s8_s3", "start_time": 27.0, "end_time": 39.0, "tag": "Step 3", "heading": "Codex Decision Tree", "description": "Apply the 4 standard questions to determine if a step is a genuine CCP."},
            {"id": "s8_s4", "start_time": 39.0, "end_time": 52.0, "tag": "Step 4", "heading": "Establish Critical Limits", "description": "Set validated, measurable parameters and operational monitoring procedures."}
        ]
    },
    {
        "slide_num": 9,
        "layout_mode": "split_photo",
        "title": "Your Work Area CCPs",
        "category": "Interactive Reflection",
        "subtitle": "Identifying and owning the Critical Control Points in your daily operational zone",
        "audio_file": "assets/audio/Slide_09_Interactive_Reflection_Your_Work_Area_CC.mp3",
        "image_file": "assets/images/slide_09.jpg",
        "elements": [
            {"id": "s9_a1", "start_time": 2.0, "end_time": 12.0, "tag": "Pasteurisation Bay", "heading": "Heat Treatment CCP", "description": "• Verify temperature (>72°C for 15s)\n• Check automated divert valve response\n• Inspect continuous chart records", "color": "danger"},
            {"id": "s9_a2", "start_time": 12.0, "end_time": 20.0, "tag": "Chilling & Storage", "heading": "Rapid Cooling CCP", "description": "• Pull down temperature to <8°C in 90 min\n• Maintain cold store below <4°C target\n• Prevent spore germination", "color": "primary"},
            {"id": "s9_a3", "start_time": 20.0, "end_time": 28.0, "tag": "Packaging Hall", "heading": "Metal Detection CCP", "description": "• 100% finished pack inline inspection\n• Hourly test piece validation (Fe/Non-Fe/SS)\n• Auto-reject fail-safe mechanism", "color": "warning"},
            {"id": "s9_act", "start_time": 28.0, "end_time": 38.0, "type": "banner", "heading": "If in Doubt: Escalate Immediately", "description": "Always notify your shift supervisor or QA manager if a parameter drifts.", "color": "accent"}
        ]
    },
    {
        "slide_num": 10,
        "layout_mode": "full_width_grid_2x4",
        "title": "Importance of HACCP for Our Company",
        "category": "Business Value",
        "subtitle": "8 fundamental reasons why HACCP safeguards our consumers, brand and licence to trade",
        "audio_file": "assets/audio/Slide_10_Importance_of_HACCP_for_Our_Company.mp3",
        "elements": [
            {"id": "s10_r1", "start_time": 2.0, "end_time": 8.0, "tag": "1. Risk Control", "heading": "Identifies & Prevents Hazards", "description": "Systematic hazard mapping across raw milk intake, processing and packing."},
            {"id": "s10_r2", "start_time": 8.0, "end_time": 14.0, "tag": "2. Safety", "heading": "Prevents Foodborne Illness", "description": "Eliminates dangerous pathogens like Listeria, Salmonella, and pathogenic E. coli."},
            {"id": "s10_r3", "start_time": 14.0, "end_time": 20.0, "tag": "3. Prevention", "heading": "Solves Root Causes", "description": "Controls process conditions directly rather than reacting to spoilage at the end."},
            {"id": "s10_r4", "start_time": 20.0, "end_time": 26.0, "tag": "4. Public Health", "heading": "Protects Public Health", "description": "Guarantees safe daily nutrition for millions of families across the UK."},
            {"id": "s10_r5", "start_time": 26.0, "end_time": 32.0, "tag": "5. Brand Trust", "heading": "Customer & Retailer Trust", "description": "Meets strict supermarket codes of practice and BRCGS food safety benchmarks."},
            {"id": "s10_r6", "start_time": 32.0, "end_time": 38.0, "tag": "6. Security", "heading": "Prevents Costly Recalls", "description": "Protects company reputation and avoids devastating product recall expenses."},
            {"id": "s10_r7", "start_time": 38.0, "end_time": 44.0, "tag": "7. Compliance", "heading": "Demonstrates Compliance", "description": "Provides verified documentation and due diligence defense during audits."},
            {"id": "s10_r8", "start_time": 44.0, "end_time": 53.0, "tag": "8. Legal Licence", "heading": "Mandatory Licence to Trade", "description": "Statutory requirement: the plant cannot legally operate without a valid HACCP plan."}
        ]
    },
    {
        "slide_num": 11,
        "layout_mode": "split_photo",
        "title": "Production CCPs: Filtration & Heat Treatment",
        "category": "Dairy Operations",
        "subtitle": "Physical sediment removal and validated thermal pathogen kill steps",
        "audio_file": "assets/audio/Slide_11_Production_CCP_Examples_Filtration_Therm.mp3",
        "image_file": "assets/images/slide_11.jpg",
        "elements": [
            {
                "id": "s11_ccp1",
                "start_time": 2.0,
                "end_time": 18.0,
                "tag": "CCP 1",
                "heading": "Raw Milk Filtration (1000 µm)",
                "description": "• In-line 1000-micron filter mesh at tanker intake\n• Removes farm sediment, straw, and foreign particulate\n• Filter integrity checked and logged before and after discharge",
                "color": "primary"
            },
            {
                "id": "s11_ccp2",
                "start_time": 18.0,
                "end_time": 48.0,
                "tag": "CCP 2",
                "heading": "HTST Pasteurisation (>72°C / 15s)",
                "description": "• Thermal kill step for Listeria monocytogenes and Salmonella\n• Automated flow divert valve triggers if temperature drops below 72.0°C\n• Continuous temperature chart recording and hourly verification",
                "color": "danger"
            },
            {
                "id": "s11_cook",
                "start_time": 48.0,
                "end_time": 64.0,
                "type": "banner",
                "heading": "Dessert & Curd Thermal Cook CCP (>86°C / 20 min)",
                "description": "Validated thermal processing for dessert bases and cooked cheese recipes.",
                "color": "success"
            }
        ]
    },
    {
        "slide_num": 12,
        "layout_mode": "split_photo",
        "title": "Production CCPs: Chilling & Metal Detection",
        "category": "Dairy Operations",
        "subtitle": "Spore germination inhibition and final packaging physical inspection",
        "audio_file": "assets/audio/Slide_12_Production_CCP_Examples_Chilling_Metal_D.mp3",
        "image_file": "assets/images/slide_12.jpg",
        "elements": [
            {
                "id": "s12_ccp3",
                "start_time": 2.0,
                "end_time": 26.0,
                "tag": "CCP 3",
                "heading": "Rapid Chilling (<8°C in 90 min)",
                "description": "• Chills pasteurised milk and curds to <8.0°C within 90 minutes\n• Target finished storage temperature below 4.0°C\n• Inhibits germination of heat-resistant Bacillus cereus spores",
                "color": "primary"
            },
            {
                "id": "s12_ccp4",
                "start_time": 26.0,
                "end_time": 43.0,
                "tag": "CCP 4",
                "heading": "In-Line Metal Detection",
                "description": "• 100% inspection of finished cheese, yogurt, and dessert packs\n• Calibrated with Ferrous, Non-Ferrous, and Stainless Steel test pieces\n• Automated reject mechanism diverts suspect packs to a locked bin",
                "color": "warning"
            }
        ]
    },
    {
        "slide_num": 13,
        "layout_mode": "split_photo",
        "title": "Monitoring Procedures & Deviation Management",
        "category": "Monitoring & GMP",
        "subtitle": "Live logging, automated divert valves, and environmental Listeria surveillance",
        "audio_file": "assets/audio/Slide_13_Monitoring_Procedures_Deviation_Manageme.mp3",
        "image_file": "assets/images/slide_13.jpg",
        "elements": [
            {"id": "s13_m1", "start_time": 2.0, "end_time": 14.0, "tag": "Real-Time Logs", "heading": "Live Shift Logging", "description": "Observations must match physical gauges. Never back-fill paperwork after the event."},
            {"id": "s13_m2", "start_time": 14.0, "end_time": 28.0, "tag": "Automated Divert", "heading": "Instant Fail-Safe Action", "description": "If pasteuriser temp < 72°C, automated divert valve immediately diverts milk to balance tank."},
            {"id": "s13_m3", "start_time": 28.0, "end_time": 36.0, "tag": "NCR Protocol", "heading": "Non-Conformance Reporting", "description": "Raise an Incident Report immediately whenever a critical limit boundary is breached."},
            {"id": "s13_m4", "start_time": 36.0, "end_time": 52.0, "tag": "Environmental Swabs", "heading": "Listeria Surveillance", "description": "Risk-based swabbing of plant drains, floors, and food contact surfaces."}
        ]
    },
    {
        "slide_num": 14,
        "layout_mode": "split_photo",
        "title": "Hazard Spotlight: Chemical Safety & CIP",
        "category": "Chemical Controls",
        "subtitle": "CIP sanitisation, Cleaning Instruction Cards (CICs), and prohibited tools",
        "audio_file": "assets/audio/Slide_14_Hazard_Spotlight_Chemical_Safety.mp3",
        "image_file": "assets/images/slide_14.jpg",
        "elements": [
            {"id": "s14_c1", "start_time": 2.0, "end_time": 14.0, "tag": "Approved Chemicals", "heading": "CIP & Sanitiser Control", "description": "Use only company-approved chemicals at verified dilutions and contact times."},
            {"id": "s14_c2", "start_time": 14.0, "end_time": 28.0, "tag": "CICs Protocol", "heading": "Cleaning Instruction Cards", "description": "Follow CICs strictly: check chemical concentration, water temperature, and contact time."},
            {"id": "s14_c3", "start_time": 28.0, "end_time": 46.0, "type": "warning_box", "tag": "Strictly Forbidden", "heading": "Prohibited Cleaning Tools", "description": "Sponges harbor bacteria. Wire scouring pads shed metal wires into dairy products. Both are banned on site.", "color": "danger"}
        ]
    },
    {
        "slide_num": 15,
        "layout_mode": "split_photo",
        "title": "Hazard Spotlight: Physical Safety",
        "category": "Physical Controls",
        "subtitle": "Foreign body eradication, site glass policy, and emergency breakage procedures",
        "audio_file": "assets/audio/Slide_15_Hazard_Spotlight_Physical_Safety.mp3",
        "image_file": "assets/images/slide_15.jpg",
        "elements": [
            {"id": "s15_p1", "start_time": 2.0, "end_time": 14.0, "tag": "Foreign Bodies", "heading": "Physical Contaminants", "description": "Glass, brittle hard plastics, metal swarf, screws, nuts, jewellery, and hair."},
            {"id": "s15_p2", "start_time": 14.0, "end_time": 26.0, "tag": "Consumer Risks", "heading": "Harm & Trauma", "description": "Choking hazards, mouth lacerations, broken teeth, and internal punctures."},
            {"id": "s15_p3", "start_time": 26.0, "end_time": 34.0, "tag": "Glass Policy", "heading": "Strict Glass Ban", "description": "Zero glass in production halls and staff canteens; daily perspex register audits."},
            {"id": "s15_p4", "start_time": 34.0, "end_time": 45.0, "tag": "Breakage Action", "heading": "Emergency Procedure", "description": "Stop the line immediately, quarantine a 30m radius of product, and notify QA at once."}
        ]
    },
    {
        "slide_num": 16,
        "layout_mode": "full_width_grid_4col",
        "title": "The 14 Major Food Allergens",
        "category": "Allergen Compliance",
        "subtitle": "UK & EU statutory mandatory declaration of all 14 recognized food allergens",
        "audio_file": "assets/audio/Slide_16_Hazard_Spotlight_Allergen_Control_The_14.mp3",
        "elements": [
            {"id": "s16_1", "start_time": 2.0, "end_time": 8.0, "tag": "Allergen 01", "heading": "1. Celery", "description": "Includes stalks, leaves, and celery salt."},
            {"id": "s16_2", "start_time": 8.0, "end_time": 14.0, "tag": "Allergen 02", "heading": "2. Gluten Cereals", "description": "Wheat, rye, barley, oats, spelt, and kamut."},
            {"id": "s16_3", "start_time": 14.0, "end_time": 19.0, "tag": "Allergen 03", "heading": "3. Crustaceans", "description": "Crabs, lobsters, prawns, and scampi."},
            {"id": "s16_4", "start_time": 19.0, "end_time": 24.0, "tag": "Allergen 04", "heading": "4. Eggs", "description": "Liquid egg, albumin, and baked dessert mixes."},
            {"id": "s16_5", "start_time": 24.0, "end_time": 29.0, "tag": "Allergen 05", "heading": "5. Fish", "description": "Fish sauces, gelatin, and fish oils."},
            {"id": "s16_6", "start_time": 29.0, "end_time": 34.0, "tag": "Allergen 06", "heading": "6. Lupin", "description": "Lupin flour and seeds in bakery items."},
            {"id": "s16_7", "start_time": 34.0, "end_time": 39.0, "tag": "Allergen 07", "heading": "7. Milk & Dairy", "description": "Core site allergen: butter, cheese, whey, yogurt.", "color": "primary"},
            {"id": "s16_8", "start_time": 39.0, "end_time": 44.0, "tag": "Allergen 08", "heading": "8. Molluscs", "description": "Mussels, oysters, squid, and snails."},
            {"id": "s16_9", "start_time": 44.0, "end_time": 48.0, "tag": "Allergen 09", "heading": "9. Mustard", "description": "Mustard liquid, powder, and seeds."},
            {"id": "s16_10", "start_time": 48.0, "end_time": 53.0, "tag": "Allergen 10", "heading": "10. Peanuts", "description": "Legume groundnuts: strict site ban.", "color": "danger"},
            {"id": "s16_11", "start_time": 53.0, "end_time": 58.0, "tag": "Allergen 11", "heading": "11. Sesame", "description": "Sesame seeds, tahini, and sesame oils.", "color": "danger"},
            {"id": "s16_12", "start_time": 58.0, "end_time": 64.0, "tag": "Allergen 12", "heading": "12. Soya", "description": "Soya lecithin in chocolate coatings."},
            {"id": "s16_13", "start_time": 64.0, "end_time": 70.0, "tag": "Allergen 13", "heading": "13. Sulphites", "description": "Preservative in fruit preparations (>10mg/kg)."},
            {"id": "s16_14", "start_time": 70.0, "end_time": 76.0, "tag": "Allergen 14", "heading": "14. Tree Nuts", "description": "Almonds, hazelnuts, walnuts, cashews, pecans.", "color": "danger"}
        ]
    },
    {
        "slide_num": 17,
        "layout_mode": "split_photo",
        "title": "Allergens on Our Dairy Site",
        "category": "Allergen Management",
        "subtitle": "Managing allergen profiles across liquid milk, cheese, desserts, and yogurt lines",
        "audio_file": "assets/audio/Slide_17_Allergen_Management_on_Our_Dairy_Process.mp3",
        "image_file": "assets/images/slide_17.jpg",
        "elements": [
            {"id": "s17_a1", "start_time": 2.0, "end_time": 14.0, "tag": "Core Allergen", "heading": "Milk & Dairy", "description": "Present across all standard milk, cheese, cream, butter, and yogurt lines."},
            {"id": "s17_a2", "start_time": 14.0, "end_time": 24.0, "tag": "Bakery Ingredients", "heading": "Gluten & Eggs", "description": "Gluten in cheesecake crumb bases; Egg in chilled custards and baked puddings."},
            {"id": "s17_a3", "start_time": 24.0, "end_time": 32.0, "tag": "Coatings & Fruit", "heading": "Soya & Sulphites", "description": "Soya lecithin in chocolate coatings; Sulphites in fruit preparations and fruit syrups."},
            {"id": "s17_a4", "start_time": 32.0, "end_time": 42.0, "tag": "Segregation Rule", "heading": "Clean-Down Protocol", "description": "Full CIP wash and validated rapid protein swab testing between recipe changeovers."}
        ]
    },
    {
        "slide_num": 18,
        "layout_mode": "split_photo",
        "title": "Strict Nut-Free Site Facility Policy",
        "category": "Site Safety Policy",
        "subtitle": "Mandatory zero-tolerance prohibition of peanuts, tree nuts, and sesame seeds",
        "audio_file": "assets/audio/Slide_18_Strict_Nut_Free_Site_Policy.mp3",
        "image_file": "assets/images/slide_18.jpg",
        "elements": [
            {
                "id": "s18_stop",
                "start_time": 2.0,
                "end_time": 12.0,
                "type": "stop_card",
                "tag": "Zero Tolerance",
                "heading": "100% Nut-Free Facility",
                "description": "• No Peanuts & Peanut Butter\n• No Almonds, Hazelnuts, Walnuts\n• No Cashews, Pecans, Pistachios\n• No Brazil nuts & Macadamias\n• No Sesame seeds & Sesame oils",
                "color": "danger"
            },
            {
                "id": "s18_rules",
                "start_time": 12.0,
                "end_time": 36.0,
                "tag": "Personal Responsibilities",
                "heading": "Check Your Snacks & Meals",
                "description": "1. Check all personal snacks, cereal bars, chocolates, and bakery items.\n2. Never bring prohibited nut items into staff canteens or lockers.\n3. Applies strictly to all employees, agency staff, contractors, and visitors.\n4. Report accidental introduction immediately to HR and QA.",
                "color": "primary"
            }
        ]
    },
    {
        "slide_num": 19,
        "layout_mode": "lab_table",
        "title": "Biological Safety & Dairy Microbial KPIs",
        "category": "Microbial Standards",
        "subtitle": "Batch release criteria and laboratory microbiological release limits",
        "audio_file": "assets/audio/Slide_19_Hazard_Spotlight_Biological_Safety_Micro.mp3",
        "elements": [
            {"id": "s19_tvc", "start_time": 2.0, "end_time": 12.0, "param": "Total Viable Count (TVC)", "target": "< 5,000 cfu/g", "action": "5,000 - 10,000 cfu/g", "reject": "> 10,000 cfu/g"},
            {"id": "s19_ent", "start_time": 12.0, "end_time": 24.0, "param": "Enterobacteriaceae", "target": "< 10 cfu/g", "action": "10 - 20 cfu/g", "reject": "≥ 20 cfu/g"},
            {"id": "s19_sta", "start_time": 24.0, "end_time": 34.0, "param": "Staphylococcus aureus", "target": "< 20 cfu/g", "action": "20 - 50 cfu/g", "reject": "> 50 cfu/g"},
            {"id": "s19_bac", "start_time": 34.0, "end_time": 44.0, "param": "Bacillus cereus", "target": "< 100 cfu/g", "action": "100 - 500 cfu/g", "reject": "> 500 cfu/g"},
            {"id": "s19_sal", "start_time": 44.0, "end_time": 52.0, "param": "Salmonella spp.", "target": "ABSENT / 25g", "action": "Zero Tolerance", "reject": "DETECTED", "color": "danger"},
            {"id": "s19_lis", "start_time": 52.0, "end_time": 68.0, "param": "Listeria monocytogenes", "target": "ABSENT / 25g", "action": "Zero Tolerance", "reject": "DETECTED", "color": "danger"}
        ]
    },
    {
        "slide_num": 20,
        "layout_mode": "split_photo",
        "title": "Personal Hygiene & 20-Second Handwashing",
        "category": "Personal Hygiene",
        "subtitle": "The primary frontline defence protecting open dairy products from contamination",
        "audio_file": "assets/audio/Slide_20_Personal_Hygiene_Handwashing_Protocol.mp3",
        "image_file": "assets/images/slide_20.jpg",
        "elements": [
            {"id": "s20_h1", "start_time": 2.0, "end_time": 12.0, "tag": "Step 1", "heading": "Wet Hands & Apply Soap", "description": "Use clean running warm water and approved antibacterial foam soap."},
            {"id": "s20_h2", "start_time": 12.0, "end_time": 20.0, "tag": "Step 2", "heading": "Scrub for 20 Seconds", "description": "Thoroughly scrub palms, backs of hands, between fingers, thumbs, and wrists."},
            {"id": "s20_h3", "start_time": 20.0, "end_time": 30.0, "tag": "Step 3", "heading": "Complete Rinse", "description": "Rinse completely under running warm water to remove all soap residue."},
            {"id": "s20_h4", "start_time": 30.0, "end_time": 40.0, "tag": "Step 4", "heading": "Dry & Sanitise", "description": "Dry with single-use paper towels and apply alcohol hand rub."}
        ]
    },
    {
        "slide_num": 21,
        "layout_mode": "split_photo",
        "title": "Factory Hygiene Zoning & Stationery Coding",
        "category": "Zoning & Access",
        "subtitle": "Strict barrier controls between raw intake, intermediate processing, and packing halls",
        "audio_file": "assets/audio/Slide_21_Area_Hygiene_Zoning_Control.mp3",
        "image_file": "assets/images/slide_21.jpg",
        "elements": [
            {"id": "s21_z1", "start_time": 2.0, "end_time": 14.0, "tag": "High-Risk (Aseptic)", "heading": "Green Pen & Stationery", "description": "Open ready-to-eat filling hall. Full captive white boots, overcoats, and positive air pressure.", "color": "success"},
            {"id": "s21_z2", "start_time": 14.0, "end_time": 24.0, "tag": "High-Care Area", "heading": "Red Pen & Stationery", "description": "Pasteurised cheese curds and yogurt processing vats. Footwear barrier and captive utensils.", "color": "danger"},
            {"id": "s21_z3", "start_time": 24.0, "end_time": 48.0, "tag": "Low-Risk / Intake", "heading": "Blue Pen & Stationery", "description": "Raw tanker intake deck, chemical store, outer packaging warehouse, and general corridors.", "color": "primary"}
        ]
    },
    {
        "slide_num": 22,
        "layout_mode": "pillar_architecture",
        "title": "Prerequisite Programmes (PRPs)",
        "category": "Foundational Hygiene",
        "subtitle": "The 7 structural pillars supporting the entire dairy HACCP food safety framework",
        "audio_file": "assets/audio/Slide_22_Prerequisite_Programmes_PRPs.mp3",
        "elements": [
            {"id": "s22_p1", "start_time": 2.0, "end_time": 8.0, "tag": "01", "heading": "Cleaning & CIP", "description": "Automated CIP cycles and titration logs."},
            {"id": "s22_p2", "start_time": 8.0, "end_time": 15.0, "tag": "02", "heading": "Hygiene & PPE", "description": "Handwashing, hairnets, and illness reporting."},
            {"id": "s22_p3", "start_time": 15.0, "end_time": 22.0, "tag": "03", "heading": "Pest Control", "description": "Bait boxes, fly killers, and contractor audits."},
            {"id": "s22_p4", "start_time": 22.0, "end_time": 29.0, "tag": "04", "heading": "Maintenance", "description": "PPM servicing and food-grade lubricants."},
            {"id": "s22_p5", "start_time": 29.0, "end_time": 36.0, "tag": "05", "heading": "Suppliers", "description": "BRCGS certified ingredients & raw milk tests."},
            {"id": "s22_p6", "start_time": 36.0, "end_time": 44.0, "tag": "06", "heading": "Allergens", "description": "Dedicated equipment and clean-down checks."},
            {"id": "s22_p7", "start_time": 44.0, "end_time": 58.0, "tag": "07", "heading": "Training", "description": "Competence assessments and refreshers."}
        ]
    },
    {
        "slide_num": 23,
        "layout_mode": "split_photo",
        "title": "Cross-Contamination & 4-Point Labelling",
        "category": "Culture & Storage",
        "subtitle": "Segregation rules and the mandatory open ingredient container labelling system",
        "audio_file": "assets/audio/Slide_23_Food_Safety_Attitude_Cross_Contamination.mp3",
        "image_file": "assets/images/slide_23.jpg",
        "elements": [
            {
                "id": "s23_seg",
                "start_time": 2.0,
                "end_time": 18.0,
                "tag": "Segregation Rules",
                "heading": "Storage & Tool Separation",
                "description": "• Separate raw milk from pasteurised products\n• Store all ingredients in sealed, dedicated tubs\n• Never place ingredient containers directly on the floor\n• Use designated colour-coded scoops for each recipe",
                "color": "primary"
            },
            {
                "id": "s23_lbl",
                "start_time": 18.0,
                "end_time": 44.0,
                "type": "label_card",
                "tag": "Mandatory Standard",
                "heading": "4-Point Container Label",
                "description": "1. Ingredient Name & Batch Code\n2. Date Opened / Thawed\n3. Secondary Use-By Date (e.g. 72h max)\n4. Operator Signature / ID Number",
                "color": "warning"
            }
        ]
    },
    {
        "slide_num": 24,
        "layout_mode": "pdca_quadrants",
        "title": "Corrective Actions & The PDCA Quality Cycle",
        "category": "Continuous Improvement",
        "subtitle": "Regaining control, investigating root causes, and standardising permanent fixes",
        "audio_file": "assets/audio/Slide_24_Corrective_Actions_The_PDCA_Cycle.mp3",
        "elements": [
            {"id": "s24_p", "start_time": 2.0, "end_time": 14.0, "tag": "Phase 1", "heading": "1. PLAN", "description": "• Define hazard analysis\n• Set critical limits & tolerances\n• Prepare SOPs and CIC cards", "color": "primary"},
            {"id": "s24_d", "start_time": 14.0, "end_time": 26.0, "tag": "Phase 2", "heading": "2. DO", "description": "• Execute HACCP procedures\n• Monitor CCPs in real-time\n• Log data accurately on shift", "color": "success"},
            {"id": "s24_c", "start_time": 26.0, "end_time": 38.0, "tag": "Phase 3", "heading": "3. CHECK", "description": "• Audit shift records\n• Calibrate thermometers\n• Review lab microbiology reports", "color": "warning"},
            {"id": "s24_a", "start_time": 38.0, "end_time": 58.0, "tag": "Phase 4", "heading": "4. ACT", "description": "• Investigate deviations\n• Standardise corrective fixes\n• Update the HACCP plan", "color": "purple"}
        ]
    },
    {
        "slide_num": 25,
        "layout_mode": "split_photo",
        "title": "The HACCP Team & Individual Legal Liability",
        "category": "Shared Accountability",
        "subtitle": "Multidisciplinary ownership, quarantine protocols, and personal statutory responsibility",
        "audio_file": "assets/audio/Slide_25_The_HACCP_Team_Responsibilities_Legal_Ac.mp3",
        "image_file": "assets/images/slide_25.jpg",
        "elements": [
            {
                "id": "s25_team",
                "start_time": 2.0,
                "end_time": 14.0,
                "tag": "HACCP Team",
                "heading": "Multidisciplinary Team",
                "description": "Operations, Quality Assurance, Engineering, Hygiene, and Warehousing working collaboratively.",
                "color": "primary"
            },
            {
                "id": "s25_hold",
                "start_time": 14.0,
                "end_time": 26.0,
                "type": "hold_tag",
                "tag": "Immediate Quarantine",
                "heading": "ON-HOLD Protocol",
                "description": "Attach physical Yellow/Red ON-HOLD tag immediately and lock batch in ERP. Only QA can release quarantined lots.",
                "color": "danger"
            },
            {
                "id": "s25_law",
                "start_time": 26.0,
                "end_time": 52.0,
                "tag": "Statutory Duty",
                "heading": "Personal Legal Liability",
                "description": "Under Regulation (EC) 852/2004, individuals can be held personally liable for falsifying records or concealing safety breaches.",
                "color": "warning"
            }
        ]
    },
    {
        "slide_num": 26,
        "layout_mode": "assessment_checklist",
        "title": "Course References & Assessment Review",
        "category": "Assessment & Close",
        "subtitle": "Statutory guidance links and 10-question evaluation checklist",
        "audio_file": "assets/audio/Slide_26_References_Knowledge_Assessment_Walkthro.mp3",
        "elements": [
            {
                "id": "s26_ref",
                "start_time": 2.0,
                "end_time": 16.0,
                "tag": "Statutory Guidance",
                "heading": "Official References",
                "description": "• Food Standards Agency (FSA): food.gov.uk\n• Codex Alimentarius Commission\n• UK Regulation (EC) No 852/2004\n• Chartered Institute of Environmental Health (CIEH)",
                "color": "primary"
            },
            {
                "id": "s26_quiz",
                "start_time": 16.0,
                "end_time": 52.0,
                "tag": "Assessment Ready",
                "heading": "10-Question Knowledge Checklist",
                "description": "Q1: HACCP definition • Q2: Preventive aim • Q3: 4 Hazard categories • Q4: Pasteurisation (>72°C/15s) • Q5: Chilling (<8°C) • Q6-Q10: Cross-contamination, 20s handwashing, 14 allergens, ON-HOLD & reporting.",
                "color": "success"
            },
            {
                "id": "s26_close",
                "start_time": 52.0,
                "end_time": 72.0,
                "type": "banner",
                "heading": "Congratulations on Completing HACCP Level 2 Excellence!",
                "description": "Thank you for your commitment to upholding world-class food and dairy safety.",
                "color": "accent"
            }
        ]
    }
]

with open("presentation/slides_data.json", "w", encoding="utf-8") as f:
    json.dump(SLIDES_CONFIG, f, indent=2, ensure_ascii=False)

with open("presentation/slides_data.js", "w", encoding="utf-8") as f:
    f.write("window.HACCP_SLIDES_DATA = " + json.dumps(SLIDES_CONFIG, indent=2, ensure_ascii=False) + ";\n")

print(f"Generated data with exact layout modes and timestamps for all {len(SLIDES_CONFIG)} slides successfully!")

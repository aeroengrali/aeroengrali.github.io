# -*- coding: utf-8 -*-
"""Static-site generator for Ali Murtaza's engineering portfolio.
Reads curated project metadata, copies referenced assets, and emits a clean,
accessible, dependency-light static site (index + per-project pages + 3D demo).
"""
import os, shutil, html

ROOT = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.normpath(os.path.join(ROOT, "..", "projects"))
OUT = ROOT
ASSETS = os.path.join(OUT, "assets", "projects")

SITE = {
    "name": "Ali Murtaza",
    "role": "Aerospace Engineering (Guidance, Navigation & Control)",
    "tagline": "Final-year BS Aerospace Engineering student building flight-control, "
               "state-estimation and simulation projects in MATLAB/Simulink and C++.",
    "location": "Islamabad, Pakistan",
    "email": "aero.engr.ali@gmail.com",
    "github": "https://github.com/aeroengrali",
    "linkedin": "https://www.linkedin.com/in/aeroengrali/",
    "grad": "BS Aerospace Engineering, Institute of Space Technology (IST), expected August 2026",
}

SKILLS = [
    ("Controls & GNC", ["Control Systems", "Guidance, Navigation & Control (GNC)",
        "PID & Cascaded Control", "State-Space Modelling", "Stability Analysis",
        "Root Locus, Bode/Nyquist"]),
    ("Estimation & Simulation", ["State Estimation & Filtering (EKF/ESKF)",
        "Sensor-model & noise simulation", "Dynamic-system modelling",
        "Modelling & Simulation", "Digital-twin concepts", "Validation-oriented modelling"]),
    ("Aerospace", ["Flight Dynamics & Stability", "Aero Vehicle Performance",
        "Spacecraft Dynamics & Control", "UAV Systems", "Propulsion fundamentals"]),
    ("Programming", ["C++ (OOP)", "C", "Python (basics)", "Numerical Methods",
        "Technical Documentation"]),
    ("Embedded & CAD", ["Digital Systems Design", "Microcontrollers (Arduino)",
        "Circuits & Electronics", "SolidWorks", "Engineering Drawing / CAD"]),
    ("Tools", ["MATLAB", "Simulink", "C++ / CMake", "Python", "SolidWorks", "Git / GitHub"]),
]

# ----------------------------------------------------------------- projects
P = []
def proj(**k): P.append(k)

proj(id="01-quadcopter-attitude-control", slug="quadcopter-attitude-control",
     title="Quadcopter Attitude Controller",
     subtitle="Cascaded PID attitude stabilisation with disturbance rejection",
     period="Apr-May 2026", cats=["GNC & Controls", "Flight Control"], featured=True,
     repo="https://github.com/aeroengrali/quadcopter-attitude-control",
     summary="A 0.5 m-class quadrotor stabilised by an outer proportional angle loop and an "
             "inner PID rate loop, with gyroscopic feedforward, actuator saturation and "
             "anti-windup. Tuned to a crisp, low-overshoot response and tested against a "
             "torque-pulse disturbance.",
     highlights=["Rise time 0.45 s, settling 0.69 s, overshoot 1.2%, steady-state error 0.07°",
                 "Disturbance pulse (0.05 N·m) recovered to <0.5° in 0.80 s",
                 "1 kHz fixed-step RK4 plant with rate-gyro noise and ±0.6 N·m saturation",
                 "Interactive 3D viewer driven by the simulated attitude"],
     tech=["MATLAB R2026a", "Cascaded PID", "RK4 integration"],
     demo="quad-demo.html",
     images=[("01_attitude_tracking.png", "Attitude tracking: roll, pitch and yaw following step commands"),
             ("02_body_rates.png", "Body angular rates vs rate setpoints"),
             ("03_control_torques.png", "Commanded control torques with saturation"),
             ("04_disturbance_rejection.png", "Roll-axis disturbance rejection")])

proj(id="02-gnss-ins-nav", slug="gnss-ins-navigation",
     title="GNSS/INS Loosely-Coupled Navigation",
     subtitle="8-state EKF fusing IMU and GPS, with online bias estimation",
     period="May 2026", cats=["Estimation & Navigation", "GNC & Controls"], featured=True,
     repo="https://github.com/aeroengrali/gnss-ins-navigation",
     summary="A strapdown inertial navigator fused with 1 Hz GPS by an Extended Kalman Filter "
             "that estimates position, velocity, heading and the IMU biases. A 25 s GPS dropout "
             "shows inertial coasting (dead reckoning) versus unaided INS drift.",
     highlights=["EKF horizontal RMS 2.5 m (below the ~3.5 m raw-GPS 2D scatter)",
                 "Dropout error bounded to ~9.5 m over 25 s; unaided INS drifts ~500 m",
                 "Gyro/accel biases recovered to within ~2% of truth",
                 "Analytic EKF Jacobian; shared mechanisation isolates the value of fusion"],
     tech=["MATLAB R2026a", "Extended Kalman Filter", "Strapdown INS"],
     images=[("01_trajectory.png", "Truth vs inertial-only vs GNSS/INS EKF trajectory"),
             ("02_position_error.png", "Position error: INS-only vs EKF with dropout shaded"),
             ("03_dropout_and_bias.png", "Dropout coasting and IMU-bias convergence")])

proj(id="03-flight-dynamics-6dof", slug="flight-dynamics-modes",
     title="6-DOF Flight Dynamics & Mode Analysis",
     subtitle="Eigenstructure of the aircraft natural modes",
     period="Mar-Apr 2026", cats=["Flight Dynamics", "GNC & Controls"], featured=False,
     repo="https://github.com/aeroengrali/flight-dynamics-modes",
     summary="Decoupled longitudinal and lateral-directional linear models of a "
             "general-aviation aircraft, with the natural modes extracted live: short-period, "
             "phugoid, Dutch roll, roll subsidence and spiral, shown in the s-plane and the "
             "time domain.",
     highlights=["Short-period ωn 3.60 rad/s, ζ 0.69; phugoid ωn 0.21 rad/s, ζ 0.08",
                 "Dutch roll ωn 2.38 rad/s, ζ 0.20; fast roll subsidence; slow stable spiral",
                 "Modes computed from the state matrices and classified automatically",
                 "Results consistent with published Navion-class values"],
     tech=["MATLAB R2026a", "Control System Toolbox", "Modal analysis"],
     images=[("01_splane_modes.png", "Natural modes on the s-plane"),
             ("02_longitudinal_modes.png", "Short-period and phugoid time responses"),
             ("03_lateral_modes.png", "Dutch roll, roll and spiral responses")])

proj(id="04-reaction-wheel-adcs", slug="reaction-wheel-adcs",
     title="Reaction-Wheel Satellite ADCS",
     subtitle="Quaternion-feedback slew with momentum management",
     period="May-Jun 2026", cats=["Spacecraft", "GNC & Controls"], featured=True,
     repo="https://github.com/aeroengrali/reaction-wheel-adcs",
     summary="A rigid spacecraft performs a 60° eigenaxis slew under a quaternion PID law with "
             "three reaction wheels, conditional-integration anti-windup, and torque/momentum "
             "limits. A constant disturbance drives a secular wheel-momentum build-up.",
     highlights=["60° slew settling under 1° in ~58 s; final pointing error 0.30°",
                 "Quaternion kinematics + nonlinear rigid-body dynamics with wheel coupling",
                 "Conditional integration prevents slew windup",
                 "Wheel-momentum build-up under disturbance motivates desaturation"],
     tech=["MATLAB R2026a", "Quaternion control", "Reaction wheels"],
     images=[("01_slew_response.png", "Eigenaxis slew error and body rates"),
             ("02_quaternion.png", "Attitude quaternion converging to command"),
             ("03_wheel_momentum.png", "Reaction-wheel momentum and torques")])

proj(id="05-gnss-spp-ekf", slug="gps-spp-ekf",
     title="GPS Single-Point Positioning + EKF",
     subtitle="A from-scratch GNSS pipeline in C++17",
     period="Jan-Feb 2026", cats=["Estimation & Navigation", "Software"], featured=True,
     repo="https://github.com/aeroengrali/gps-spp-ekf",
     summary="A GPS-only pseudorange positioning engine in modern C++17: RINEX 3.x parsing, "
             "broadcast orbit/clock modelling, weighted least squares and an EKF, validated "
             "against precise IGS SP3 orbits with an independent Python audit.",
     highlights=["Full-day EKF 3D RMS 2.03 m, improving on least squares (2.52 m)",
                 "Broadcast orbits agree with precise IGS SP3 to a few metres (95th-pct 3D 2.37 m)",
                 "RINEX 3.x observation/navigation parsing, ephemeris health/fit checks",
                 "Deterministic tests plus an independent Python results audit"],
     tech=["C++17", "CMake / Ninja", "RINEX, SP3", "EKF & WLS"],
     images=[("01_accuracy.png", "GPS-only SPP+EKF accuracy vs precise IGS products")])

proj(id="06-ultrasonic-tracker", slug="ultrasonic-pan-tilt-tracker",
     title="Ultrasonic Pan-Tilt Object Tracker",
     subtitle="Scan-and-track on Arduino Mega 2560",
     period="2024", cats=["Embedded"], featured=False,
     repo="https://github.com/aeroengrali/ultrasonic-pan-tilt-tracker",
     summary="An embedded sonar-guided tracker: three HC-SR04 ultrasonic sensors feed a control "
             "loop that drives a dual-servo pan/tilt head to centre the nearest object, with a "
             "raster search sweep when no target is in range.",
     highlights=["Arduino Mega 2560, 3× HC-SR04 (5 V, 2-400 cm), dual servos, LED",
                 "Multi-sensor bearing estimation from left/centre/right ranges",
                 "Closed-loop pan/tilt actuation with a search/track state machine",
                 "Real-time embedded C/C++ on constrained hardware"],
     tech=["Arduino (C/C++)", "HC-SR04 sonar", "Servo control"],
     images=[("diagram.svg", "Sense → decide → actuate pipeline of the ultrasonic tracker")])

proj(id="07-cpp-banking", slug="cpp-banking-system",
     title="C++ Banking System (OOP)",
     subtitle="Encapsulated accounts with MPIN authentication",
     period="Nov 2022", cats=["Software"], featured=False,
     repo="https://github.com/aeroengrali/cpp-banking-system",
     summary="A console banking application built on object-oriented principles: a bankAccount "
             "class encapsulates balance and MPIN with guarded deposit, withdrawal and "
             "authenticated login. A four-person academic team project.",
     highlights=["Object-oriented design: encapsulation, accessors, validation",
                 "MPIN-authenticated login flow",
                 "Policy, security-awareness and terms modules",
                 "Team of four (Ali contributed the class design and core account logic)"],
     tech=["C++", "OOP", "Standard library"],
     images=[("diagram.svg", "Class and flow overview of the banking system")])

proj(id="08-a320-cad", slug="a320-solidworks",
     title="Airbus A320 SolidWorks CAD",
     subtitle="Solid model with dimensioned drawings and renders",
     period="Jul 2024", cats=["CAD"], featured=False,
     repo="https://github.com/aeroengrali/a320-solidworks",
     summary="An A320-class airliner modelled in SolidWorks, with a full multi-view engineering "
             "drawing (dimensioned top/side blueprints) and isometric renders. An independent "
             "CAD exercise from public reference dimensions, no manufacturer data.",
     highlights=["Parametric solid modelling of the fuselage and wing form",
                 "Dimensioned three-view engineering blueprint",
                 "Isometric and in-scene renders of the model",
                 "Built from public reference dimensions; no Airbus proprietary data"],
     tech=["SolidWorks", "Engineering drawing", "Rendering"],
     images=[("A320_drawing-10.png", "Rendered 3D views of the A320 model"),
             ("A320_drawing-05.png", "Dimensioned top and side blueprints")])

proj(id="09-morphobot-fyp", slug="morphobot-digital-twin",
     title="Rover-Hover Morphobot Digital Twin",
     subtitle="Final-year project (in progress)",
     period="2025-2026", cats=["GNC & Controls", "Flight Control"], featured=True, repo=None,
     summary="A MATLAB/Simulink digital twin of a two-mode rover ↔ hover transforming "
             "quadcopter whose motors sit inside its wheels. Covers flight dynamics, cascaded "
             "PID flight control, ESKF state estimation, skid-steer control and a mode-transition "
             "supervisor, paired with vendor-built hardware.",
     highlights=["Two-mode transforming platform: flying quad and ground rover",
                 "Cascaded PID flight control and ESKF state estimation",
                 "Mode supervisor and controlled hover ↔ rover transition",
                 "Hardware-paired digital-twin workflow (motor-in-wheel build)"],
     tech=["MATLAB / Simulink", "Stateflow"],
     note="High-level entry. Quantitative results and the full thesis are withheld until the FYP is defended.",
     images=[("contact_sheet.png", "CAD part set of the transforming quadcopter"),
             ("hardware_01.jpg", "Motor-in-wheel hardware assembly"),
             ("hardware_03.jpg", "Physical build of the morphobot")])

# ------------------------------------------------------------- SVG diagrams
SVG_TRACKER = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 280" role="img" aria-label="Sense, decide, actuate pipeline">
<rect width="760" height="280" fill="#0b1f33"/>
<style>.b{fill:#12324f;stroke:#3b82c4;stroke-width:2;rx:10}.t{fill:#e8f1fb;font:600 16px system-ui;text-anchor:middle}.s{fill:#9cc3e6;font:13px system-ui;text-anchor:middle}.a{stroke:#5fa8e0;stroke-width:2.5;marker-end:url(#ar);fill:none}</style>
<defs><marker id="ar" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#5fa8e0"/></marker></defs>
<rect class="b" x="30" y="90" width="170" height="100" rx="10"/><text class="t" x="115" y="125">3× HC-SR04</text><text class="s" x="115" y="150">ultrasonic ranges</text><text class="s" x="115" y="168">L / C / R</text>
<rect class="b" x="295" y="90" width="170" height="100" rx="10"/><text class="t" x="380" y="120">Decision logic</text><text class="s" x="380" y="144">nearest-bearing</text><text class="s" x="380" y="162">search / track</text>
<rect class="b" x="560" y="90" width="170" height="100" rx="10"/><text class="t" x="645" y="125">Pan/Tilt servos</text><text class="s" x="645" y="150">centre target</text><text class="s" x="645" y="168">+ LED status</text>
<line class="a" x1="200" y1="140" x2="290" y2="140"/><line class="a" x1="465" y1="140" x2="555" y2="140"/>
<text class="s" x="380" y="40" style="font:600 17px system-ui;fill:#e8f1fb">Arduino Mega 2560: real-time scan-and-track loop</text>
</svg>'''

SVG_BANK = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300" role="img" aria-label="Banking system class and flow">
<rect width="760" height="300" fill="#0b1f33"/>
<style>.b{fill:#12324f;stroke:#3b82c4;stroke-width:2}.t{fill:#e8f1fb;font:600 15px system-ui}.s{fill:#9cc3e6;font:13px system-ui}.a{stroke:#5fa8e0;stroke-width:2.5;marker-end:url(#ar2);fill:none}</style>
<defs><marker id="ar2" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#5fa8e0"/></marker></defs>
<rect class="b" x="40" y="60" width="240" height="180" rx="10"/>
<text class="t" x="60" y="90">class bankAccount</text><line x1="40" y1="100" x2="280" y2="100" stroke="#3b82c4"/>
<text class="s" x="60" y="125">- MPIN : int</text><text class="s" x="60" y="148">- balance : double</text><text class="s" x="60" y="171">- name, regno</text>
<text class="s" x="60" y="200">+ deposit() / withdraw()</text><text class="s" x="60" y="222">+ login(MPIN)</text>
<rect class="b" x="430" y="50" width="290" height="50" rx="8"/><text class="s" x="450" y="80">Login (MPIN authentication)</text>
<rect class="b" x="430" y="120" width="290" height="50" rx="8"/><text class="s" x="450" y="150">Deposit / Withdraw / Balance</text>
<rect class="b" x="430" y="190" width="290" height="50" rx="8"/><text class="s" x="450" y="220">Policy · Security · Terms</text>
<line class="a" x1="280" y1="150" x2="425" y2="75"/><line class="a" x1="280" y1="150" x2="425" y2="145"/><line class="a" x1="280" y1="150" x2="425" y2="215"/>
</svg>'''

def esc(s): return html.escape(str(s), quote=True)

def copy_assets():
    if os.path.exists(ASSETS): shutil.rmtree(ASSETS)
    for p in P:
        dst = os.path.join(ASSETS, p["slug"]); os.makedirs(dst, exist_ok=True)
        srcdir = os.path.join(PROJ, p["id"], "assets")
        # locate each referenced image anywhere under the project's assets tree
        for fn, _ in p["images"]:
            if fn == "diagram.svg":
                svg = SVG_TRACKER if "tracker" in p["slug"] else SVG_BANK
                with open(os.path.join(dst, fn), "w", encoding="utf-8") as f: f.write(svg)
                continue
            found = None
            for base, _d, files in os.walk(srcdir):
                if fn in files: found = os.path.join(base, fn); break
            if found: shutil.copy2(found, os.path.join(dst, fn))
            else: print("  MISSING asset:", p["slug"], fn)
        # quad trajectory CSV for the 3D demo
        if p["slug"] == "quadcopter-attitude-control":
            csv = None
            for base,_d,files in os.walk(srcdir):
                if "attitude_trajectory.csv" in files: csv=os.path.join(base,"attitude_trajectory.csv")
            if csv: shutil.copy2(csv, os.path.join(dst, "attitude_trajectory.csv"))

# ------------------------------------------------------------------ markup
def head(title, desc, depth=0):
    up = "../" * depth
    return f'''<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="stylesheet" href="{up}style.css">
</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="wrap navin">
<a class="brand" href="{up}index.html">Ali&nbsp;Murtaza</a>
<nav aria-label="Primary"><a href="{up}index.html#projects">Projects</a><a href="{up}index.html#skills">Skills</a><a href="{up}index.html#about">About</a><a href="{up}index.html#contact">Contact</a></nav>
</div></header>'''

FOOT = lambda depth=0: f'''<footer class="foot" id="contact"><div class="wrap">
<h2>Contact</h2>
<p>Open to GNC, flight-control, simulation and aerospace R&amp;D roles, internships and graduate study.</p>
<p class="links">
<a href="mailto:{SITE['email']}">{SITE['email']}</a> ·
<a href="{SITE['github']}" rel="noopener">GitHub</a> ·
<a href="{SITE['linkedin']}" rel="noopener">LinkedIn</a> ·
<span>{esc(SITE['location'])}</span></p>
<p class="fine">© 2026 Ali Murtaza · {esc(SITE['grad'])}</p>
</div></footer></body></html>'''

def card(p):
    hero, alt = p["images"][0]
    tags = "".join(f'<span class="tag">{esc(c)}</span>' for c in p["cats"])
    feat = '<span class="badge">Featured</span>' if p.get("featured") else ""
    cats_attr = " ".join(p["cats"])
    return f'''<a class="card" href="projects/{p['slug']}.html" data-cats="{esc(cats_attr)}">
<div class="card-img"><img loading="lazy" src="assets/projects/{p['slug']}/{hero}" alt="{esc(alt)}"></div>
<div class="card-body"><div class="card-top">{feat}<span class="period">{esc(p['period'])}</span></div>
<h3>{esc(p['title'])}</h3><p class="sub">{esc(p['subtitle'])}</p>
<div class="tags">{tags}</div></div></a>'''

def build_index():
    cats = ["All", "GNC & Controls", "Estimation & Navigation", "Flight Control",
            "Flight Dynamics", "Spacecraft", "Software", "Embedded", "CAD"]
    chips = "".join(f'<button class="chip{" on" if c=="All" else ""}" data-filter="{esc(c)}">{esc(c)}</button>' for c in cats)
    cards = "\n".join(card(p) for p in P)
    skills = ""
    for grp, items in SKILLS:
        lis = "".join(f"<li>{esc(i)}</li>" for i in items)
        skills += f'<div class="skill"><h3>{esc(grp)}</h3><ul>{lis}</ul></div>'
    doc = head(f"{SITE['name']} | {SITE['role']}", SITE["tagline"])
    doc += f'''
<main id="main">
<section class="hero">
<div class="hero-svg" aria-hidden="true">{HERO_SVG}</div>
<div class="wrap">
<p class="eyebrow">{esc(SITE['role'])}</p>
<h1>{esc(SITE['name'])}</h1>
<p class="lede">{esc(SITE['tagline'])}</p>
<p class="hero-meta">{esc(SITE['grad'])}</p>
<div class="cta"><a class="btn" href="#projects">View projects</a>
<a class="btn ghost" href="{SITE['github']}" rel="noopener">GitHub</a></div>
</div></section>

<section id="projects" class="sec"><div class="wrap">
<h2>Projects</h2>
<p class="sec-lede">Flight control, state estimation, navigation, flight dynamics, spacecraft attitude control, software and CAD. Each card opens a detailed write-up with results.</p>
<div class="filters" role="group" aria-label="Filter projects by area">{chips}</div>
<div class="grid">{cards}</div>
</div></section>

<section id="skills" class="sec alt"><div class="wrap">
<h2>Skills</h2>
<div class="skills">{skills}</div>
</div></section>

<section id="about" class="sec"><div class="wrap about">
<h2>About</h2>
<p>I am a final-year BS Aerospace Engineering student at the Institute of Space Technology, Islamabad, focused on guidance, navigation and control. I build flight-control, estimation and simulation systems in MATLAB/Simulink and C++, and I care about getting the engineering right: honest models, verified results, and clear documentation.</p>
<p>Recent work spans cascaded flight control, a GNSS/INS navigation filter built around an Extended Kalman Filter, aircraft mode analysis, spacecraft attitude control, and a from-scratch GNSS positioning engine in C++. My final-year project is a hardware-paired digital twin of a transforming rover-hover quadcopter.</p>
</div></section>
</main>
'''
    doc += FOOT()
    doc += '<script src="app.js"></script>'
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f: f.write(doc)

def build_project(p):
    hero, halt = p["images"][0]
    gallery = ""
    for fn, alt in p["images"]:
        gallery += f'<figure><img loading="lazy" src="../assets/projects/{p["slug"]}/{fn}" alt="{esc(alt)}"><figcaption>{esc(alt)}</figcaption></figure>'
    hl = "".join(f"<li>{esc(h)}</li>" for h in p["highlights"])
    tech = "".join(f'<span class="tag">{esc(t)}</span>' for t in p["tech"])
    cats = "".join(f'<span class="tag alt">{esc(c)}</span>' for c in p["cats"])
    links = ""
    if p.get("repo"): links += f'<a class="btn" href="{esc(p["repo"])}" rel="noopener">Source on GitHub</a>'
    if p.get("demo"): links += f'<a class="btn ghost" href="{esc(p["demo"])}">Open 3D demo</a>'
    note = f'<p class="note">{esc(p["note"])}</p>' if p.get("note") else ""
    demo = ""
    if p.get("demo"):
        demo = f'<section class="psec"><h2>Interactive 3D</h2><iframe class="demo" src="{esc(p["demo"])}" title="Interactive 3D attitude viewer" loading="lazy"></iframe></section>'
    doc = head(f'{p["title"]} | {SITE["name"]}', p["summary"], depth=1)
    doc += f'''
<main id="main" class="proj">
<div class="wrap">
<p class="crumb"><a href="../index.html#projects">← All projects</a></p>
<p class="eyebrow">{esc(p['period'])}</p>
<h1>{esc(p['title'])}</h1>
<p class="lede">{esc(p['subtitle'])}</p>
<div class="tags">{cats}</div>
<p class="overview">{esc(p['summary'])}</p>
{note}
<div class="cta">{links}</div>

<section class="psec"><h2>Highlights</h2><ul class="hl">{hl}</ul></section>
{demo}
<section class="psec"><h2>Results &amp; figures</h2><div class="gallery">{gallery}</div></section>
<section class="psec"><h2>Built with</h2><div class="tags">{tech}</div></section>
</div></main>
'''
    doc += FOOT(1)
    with open(os.path.join(OUT, "projects", f'{p["slug"]}.html'), "w", encoding="utf-8") as f: f.write(doc)

HERO_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" preserveAspectRatio="xMidYMid slice">
<defs><radialGradient id="g" cx="70%" cy="30%" r="80%"><stop offset="0%" stop-color="#1b4a73"/><stop offset="100%" stop-color="#081522"/></radialGradient></defs>
<rect width="1200" height="400" fill="url(#g)"/>
<g fill="none" stroke="#3b82c4" stroke-width="1.4" opacity="0.5">
<ellipse cx="850" cy="150" rx="320" ry="120" transform="rotate(-18 850 150)"/>
<ellipse cx="850" cy="150" rx="230" ry="80" transform="rotate(-18 850 150)"/>
<ellipse cx="850" cy="150" rx="140" ry="48" transform="rotate(-18 850 150)"/></g>
<g stroke="#5fa8e0" stroke-width="2" opacity="0.7" fill="none">
<path d="M40 360 C 300 300, 500 260, 760 120"/></g>
<circle cx="760" cy="120" r="6" fill="#9cc3e6"/><circle cx="850" cy="150" r="9" fill="#e8f1fb"/>
<g fill="#6fb0e6" opacity="0.6"><circle cx="180" cy="80" r="2"/><circle cx="320" cy="180" r="2"/><circle cx="120" cy="250" r="2"/><circle cx="500" cy="90" r="2"/><circle cx="1050" cy="300" r="2"/></g>
</svg>'''

def build_demo():
    src = '''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Quadcopter attitude (3D demo)</title>
<style>html,body{margin:0;height:100%;background:#0b1f33;color:#cfe2f5;font:14px system-ui;overflow:hidden}
#hud{position:fixed;left:12px;top:10px;background:rgba(8,21,34,.7);padding:8px 12px;border-radius:8px;line-height:1.5}
#hud b{color:#fff}.sr{position:absolute;left:-9999px;top:auto}</style></head><body>
<h1 class="sr">Quadcopter Attitude Control: Interactive 3D Demo</h1>
<div id="hud">Quadcopter attitude (simulated)<br><span id="t">t = 0.0 s</span> · <span id="rpy">roll 0° pitch 0° yaw 0°</span><br><span style="opacity:.7">drag to orbit · loops automatically</span></div>
<script type="module">
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';
import {OrbitControls} from 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/controls/OrbitControls.js';
const scene=new THREE.Scene(); scene.background=new THREE.Color(0x0b1f33);
const cam=new THREE.PerspectiveCamera(50,innerWidth/innerHeight,0.1,100); cam.position.set(3.2,2.4,3.6);
const rnd=new THREE.WebGLRenderer({antialias:true}); rnd.setSize(innerWidth,innerHeight); rnd.setPixelRatio(Math.min(devicePixelRatio,2)); document.body.appendChild(rnd.domElement);
const ctr=new OrbitControls(cam,rnd.domElement); ctr.enableDamping=true; ctr.enablePan=false;
scene.add(new THREE.AmbientLight(0xffffff,0.7)); const d=new THREE.DirectionalLight(0xffffff,1.1); d.position.set(5,8,4); scene.add(d);
const grid=new THREE.GridHelper(12,12,0x274a66,0x18324a); scene.add(grid);
scene.add(new THREE.AxesHelper(1.6));
// quad: central body + 4 arms + rotors
const quad=new THREE.Group();
const bodyMat=new THREE.MeshStandardMaterial({color:0x2c3e50,metalness:.3,roughness:.5});
const armMat=new THREE.MeshStandardMaterial({color:0x34495e});
const rotorMat=[0xd92a2a,0x1a73b8,0x2aa14e,0xeab308].map(c=>new THREE.MeshStandardMaterial({color:c}));
quad.add(new THREE.Mesh(new THREE.BoxGeometry(0.5,0.16,0.5),bodyMat));
const L=1.0; const pos=[[L,L],[-L,L],[-L,-L],[L,-L]];
pos.forEach((p,i)=>{const a=new THREE.Mesh(new THREE.BoxGeometry(0.07,0.05,1.4),armMat);
 a.position.set(p[0]/2,0,p[1]/2); a.lookAt(0,0,0); quad.add(a);
 const r=new THREE.Mesh(new THREE.CylinderGeometry(0.34,0.34,0.03,28),rotorMat[i]);
 r.position.set(p[0],0.09,p[1]); r.userData.spin=true; quad.add(r);});
scene.add(quad);
let traj=[[0,0,0,0]];
fetch('attitude_trajectory.csv').then(r=>r.text()).then(t=>{
 traj=t.trim().split(/\\r?\\n/).map(l=>l.split(',').map(Number)).filter(a=>a.length>=4&&!isNaN(a[0]));
}).catch(()=>{});
const tEl=document.getElementById('t'), rpyEl=document.getElementById('rpy');
let k=0, last=performance.now(), acc=0;
function frame(now){requestAnimationFrame(frame);
 const dt=(now-last)/1000; last=now; acc+=dt;
 if(traj.length>1){ if(acc>0.04){acc=0; k=(k+1)%traj.length;}
  const [tt,roll,pitch,yaw]=traj[k];
  quad.rotation.set(THREE.MathUtils.degToRad(roll),THREE.MathUtils.degToRad(yaw),THREE.MathUtils.degToRad(pitch),'XYZ');
  tEl.textContent='t = '+tt.toFixed(1)+' s';
  rpyEl.textContent=`roll ${roll.toFixed(0)}° pitch ${pitch.toFixed(0)}° yaw ${yaw.toFixed(0)}°`;}
 quad.children.forEach(c=>{if(c.userData.spin)c.rotation.y+=0.4;});
 ctr.update(); rnd.render(scene,cam);}
requestAnimationFrame(frame);
addEventListener('resize',()=>{cam.aspect=innerWidth/innerHeight;cam.updateProjectionMatrix();rnd.setSize(innerWidth,innerHeight);});
</script></body></html>'''
    with open(os.path.join(OUT, "quad-demo.html"), "w", encoding="utf-8") as f: f.write(src)

if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "projects"), exist_ok=True)
    copy_assets()
    build_index()
    for p in P: build_project(p)
    build_demo()
    print("Site generated:", len(P), "project pages + index + demo")

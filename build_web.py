# -*- coding: utf-8 -*-
"""Portfolio site generator v2: branded SVG design system (consistent card
headers, per-project flow diagrams, favicon, OG image) + richer multi-section
project pages with deliberately curated figures. Dependency-free static site."""
import os, shutil, html

ROOT = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.normpath(os.path.join(ROOT, "..", "projects"))
OUT = ROOT
APROOT = os.path.join(OUT, "assets", "projects")

SITE = {
    "name": "Ali Murtaza",
    "role": "Aerospace Engineering (Guidance, Navigation & Control)",
    "tagline": "Final-year BS Aerospace Engineering student building flight-control, "
               "state-estimation and simulation projects in MATLAB/Simulink and C++.",
    "location": "Islamabad, Pakistan",
    "email": "aero.engr.ali@gmail.com",
    "github": "https://github.com/aeroengrali",
    "linkedin": "https://www.linkedin.com/in/aeroengrali/",
    "url": "https://aeroengrali.github.io",
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

def esc(s): return html.escape(str(s), quote=True)

# ----------------------------------------------------------------- projects
P = []
def proj(**k): P.append(k)

proj(id="01-quadcopter-attitude-control", slug="quadcopter-attitude-control",
     num="01", title="Quadcopter Attitude Controller",
     subtitle="Cascaded PID attitude stabilisation with disturbance rejection",
     period="Apr-May 2026", cats=["Flight Control", "GNC & Controls"],
     accent="#2f7fd1", family="orbit", featured=True,
     repo="https://github.com/aeroengrali/quadcopter-attitude-control",
     demo="quad-demo.html",
     overview="A 0.5 m-class quadrotor stabilised by a cascaded controller: an outer "
              "proportional angle loop sets body-rate targets, and an inner PID rate loop "
              "produces the control torques, with gyroscopic feedforward, actuator saturation "
              "and anti-windup.",
     challenge="A quadrotor's attitude is open-loop unstable and cross-coupled. The controller "
               "has to be fast yet low-overshoot, and hold attitude when an external torque hits.",
     approach=["Outer P angle loop generates roll/pitch/yaw rate setpoints",
               "Inner PID rate loop tracks them and commands body torques",
               "Gyroscopic decoupling feedforward and torque saturation modelled",
               "Tuned for a crisp response, then tested with a torque-pulse disturbance"],
     flow=["Angle ref", "Outer P loop", "Inner PID rate loop", "Saturation + gyro FF", "Quad plant"],
     metrics=[("Rise time (10-90%)", "0.45 s"), ("Settling (2%)", "0.69 s"),
              ("Overshoot", "1.2%"), ("Steady-state error", "0.07 deg"),
              ("Disturbance recovery", "0.80 s")],
     outcomes="Demonstrates cascaded flight-control architecture, PID tuning for a low-overshoot "
              "response, actuator saturation and anti-windup handling, and quantitative evaluation.",
     tech=["MATLAB R2026a", "Cascaded PID", "RK4 integration"],
     figs=[("01-quadcopter-attitude-control", "01_attitude_tracking.png",
            "Roll, pitch and yaw track their step commands; the bump near t = 3.5 s is the injected disturbance being rejected."),
           ("01-quadcopter-attitude-control", "04_disturbance_rejection.png",
            "Roll-axis recovery from a 0.05 N.m torque pulse: peak deviation 4.07 deg, back under 0.5 deg in 0.80 s.")])

proj(id="02-gnss-ins-nav", slug="gnss-ins-navigation",
     num="02", title="GNSS/INS Loosely-Coupled Navigation",
     subtitle="8-state EKF fusing IMU and GPS, with online bias estimation",
     period="May 2026", cats=["Estimation & Navigation", "GNC & Controls"],
     accent="#1aa37a", family="path", featured=True,
     repo="https://github.com/aeroengrali/gnss-ins-navigation",
     overview="A planar strapdown inertial navigator fused with 1 Hz GPS by an Extended Kalman "
              "Filter that estimates position, velocity, heading and the IMU biases, so inertial "
              "errors are observed rather than left to accumulate.",
     challenge="Inertial navigation drifts without bound; GPS is accurate but slow and can drop out. "
               "The filter must fuse both and keep navigating when GPS disappears.",
     approach=["Strapdown mechanisation integrates the noisy, biased IMU",
               "8-state EKF (position, velocity, heading, gyro and accel biases) with analytic Jacobian",
               "1 Hz GPS position updates correct the state and observe the biases",
               "A 25 s GPS dropout tests inertial coasting (dead reckoning)"],
     flow=["IMU (biased)", "Strapdown INS", "EKF predict", "GPS update (1 Hz)", "Fused estimate"],
     metrics=[("EKF horizontal RMS", "2.50 m"), ("Max error in 25 s dropout", "9.5 m"),
              ("Gyro bias recovered", "0.51 vs 0.50 deg/s"), ("Unaided INS drift", "496 m")],
     outcomes="Demonstrates strapdown INS, EKF design with an analytic Jacobian, loosely-coupled "
              "fusion, online IMU-bias observability, and graceful degradation during outages.",
     tech=["MATLAB R2026a", "Extended Kalman Filter", "Strapdown INS"],
     figs=[("02-gnss-ins-nav", "01_trajectory.png",
            "Truth versus inertial-only drift versus the fused GNSS/INS estimate over a 120 s run."),
           ("02-gnss-ins-nav", "03_dropout_and_bias.png",
            "Top: the EKF coasts through a 25 s GPS outage and snaps back. Bottom: the estimated IMU biases converge to the true values.")])

proj(id="03-flight-dynamics-6dof", slug="flight-dynamics-modes",
     num="03", title="6-DOF Flight Dynamics & Mode Analysis",
     subtitle="Eigenstructure of the aircraft natural modes",
     period="Mar-Apr 2026", cats=["Flight Dynamics", "GNC & Controls"],
     accent="#7b61ff", family="wave", featured=False,
     repo="https://github.com/aeroengrali/flight-dynamics-modes",
     overview="Decoupled longitudinal and lateral-directional linear state-space models of a "
              "general-aviation aircraft, with the natural modes extracted live and shown in both "
              "the s-plane and the time domain.",
     challenge="An aircraft's handling is governed by a handful of natural modes. The task is to "
               "build the linear models and characterise each mode's frequency, damping and shape.",
     approach=["Assemble the longitudinal [u, w, q, theta] and lateral [beta, p, r, phi] state matrices",
               "Compute eigenvalues, damping and natural frequencies",
               "Classify automatically into short-period, phugoid, Dutch roll, roll and spiral",
               "Excite each mode with an initial-condition response"],
     flow=["Stability derivatives", "State matrices", "Eigenanalysis", "Mode classification", "s-plane + time response"],
     metrics=[("Short-period", "wn 3.60, zeta 0.69"), ("Phugoid", "wn 0.21, zeta 0.08"),
              ("Dutch roll", "wn 2.38, zeta 0.20"), ("Roll / spiral", "t_half 0.08 s / 77.6 s")],
     outcomes="Demonstrates linear flight-dynamics modelling, modal (eigenstructure) analysis, and "
              "interpretation of handling-quality modes in frequency and time.",
     tech=["MATLAB R2026a", "Control System Toolbox", "Modal analysis"],
     figs=[("03-flight-dynamics-6dof", "01_splane_modes.png",
            "All five natural modes on the s-plane: stable, with characteristic frequencies and damping."),
           ("03-flight-dynamics-6dof", "02_longitudinal_modes.png",
            "Longitudinal response: the fast short-period and the slow, lightly-damped phugoid."),
           ("03-flight-dynamics-6dof", "03_lateral_modes.png",
            "Lateral-directional response: Dutch roll, fast roll subsidence, and the slow spiral.")])

proj(id="04-reaction-wheel-adcs", slug="reaction-wheel-adcs",
     num="04", title="Reaction-Wheel Satellite ADCS",
     subtitle="Quaternion-feedback slew with momentum management",
     period="May-Jun 2026", cats=["Spacecraft", "GNC & Controls"],
     accent="#e0a82e", family="sat", featured=True,
     repo="https://github.com/aeroengrali/reaction-wheel-adcs",
     overview="A rigid spacecraft performs a 60 deg eigenaxis slew under a quaternion PID law with "
              "three reaction wheels, conditional-integration anti-windup, and torque and momentum "
              "limits.",
     challenge="Spacecraft attitude lives on the quaternion manifold and the actuators (wheels) "
               "saturate and accumulate momentum. The controller must slew accurately without windup.",
     approach=["Quaternion kinematics with full nonlinear rigid-body + wheel dynamics",
               "Quaternion-error PID feedback drives a 60 deg eigenaxis slew",
               "Conditional integration prevents wind-up during the large-angle transient",
               "A constant disturbance reveals secular wheel-momentum build-up"],
     flow=["Attitude error (quaternion)", "PID + anti-windup", "Wheel torque (limited)", "Rigid-body dynamics", "Momentum tracking"],
     metrics=[("Slew", "60 deg eigenaxis"), ("Settling (<1 deg)", "57.9 s"),
              ("Final pointing error", "0.30 deg"), ("Peak body rate", "2.77 deg/s")],
     outcomes="Demonstrates quaternion attitude control, nonlinear rigid-body dynamics with wheel "
              "coupling, anti-windup, actuator saturation, and reaction-wheel momentum management.",
     tech=["MATLAB R2026a", "Quaternion control", "Reaction wheels"],
     figs=[("04-reaction-wheel-adcs", "01_slew_response.png",
            "The 60 deg slew settles under 1 deg in about 58 s with a smooth, low-rate profile."),
           ("04-reaction-wheel-adcs", "03_wheel_momentum.png",
            "Wheel momentum builds steadily under the disturbance, the trigger for a desaturation cycle on a real mission.")])

proj(id="05-gnss-spp-ekf", slug="gps-spp-ekf",
     num="05", title="GPS Single-Point Positioning + EKF",
     subtitle="A from-scratch GNSS pipeline in C++17",
     period="Jan-Feb 2026", cats=["Estimation & Navigation", "Software"],
     accent="#16967f", family="path", featured=True,
     repo="https://github.com/aeroengrali/gps-spp-ekf",
     overview="A GPS-only pseudorange positioning engine in modern C++17: RINEX 3.x parsing, "
              "broadcast orbit and clock modelling, weighted least squares and an EKF, validated "
              "against precise IGS SP3 orbits with an independent Python audit.",
     challenge="Turning raw RINEX observations into a position fix means modelling satellite orbits "
               "and clocks from the navigation message and estimating the receiver state robustly.",
     approach=["Parse RINEX 3.x observation and navigation files (priority/fallback selection)",
               "Model broadcast orbits and clocks (Kepler, relativistic, Earth-rotation corrections)",
               "Estimate position with weighted least squares and an EKF",
               "Validate against precise IGS SP3 orbits; deterministic tests + independent audit"],
     flow=["RINEX 3.x", "Broadcast orbits/clocks", "WLS + EKF", "SP3 validation", "Position fix"],
     metrics=[("Full-day LS 3D RMS", "2.52 m"), ("Full-day EKF 3D RMS", "2.03 m"),
              ("SP3 95th-pct 3D", "2.37 m"), ("Language", "C++17 (CMake/Ninja)")],
     outcomes="Demonstrates from-scratch GNSS engineering: file parsing, orbit/clock modelling, "
              "least-squares and Kalman estimation, validation, and disciplined testing in C++.",
     tech=["C++17", "CMake / Ninja", "RINEX, SP3", "EKF & WLS"],
     figs=[("05-gnss-spp-ekf", "01_accuracy.png",
            "Full-day acceptance run: the EKF improves on least squares, and broadcast orbits agree with precise IGS products to a few metres.")])

proj(id="06-ultrasonic-tracker", slug="ultrasonic-pan-tilt-tracker",
     num="06", title="Ultrasonic Pan-Tilt Object Tracker",
     subtitle="Scan-and-track on Arduino Mega 2560",
     period="2024", cats=["Embedded"],
     accent="#e8743b", family="circuit", featured=False,
     repo="https://github.com/aeroengrali/ultrasonic-pan-tilt-tracker",
     overview="An embedded sonar-guided tracker: three HC-SR04 ultrasonic sensors feed a control "
              "loop that drives a dual-servo pan/tilt head to centre the nearest object, with a "
              "raster search sweep when no target is in range.",
     challenge="With only three cheap range sensors and a microcontroller, infer where the nearest "
               "object is and keep a pan/tilt head pointed at it in real time.",
     approach=["Three HC-SR04 sensors give left/centre/right distances via echo timing",
               "Decision logic finds the bearing of the closest in-range object",
               "Dual servos pan and tilt to centre the target; an LED signals lock",
               "A raster search sweep runs when nothing is in range"],
     flow=["3x HC-SR04", "Bearing logic", "Search / track state", "Pan + tilt servos", "LED status"],
     metrics=[("Platform", "Arduino Mega 2560"), ("Sensors", "3x HC-SR04 (2-400 cm)"),
              ("Actuation", "dual-servo pan/tilt"), ("Language", "C/C++")],
     outcomes="Demonstrates embedded real-time sensing, multi-sensor bearing estimation, closed-loop "
              "actuator control, and a search/track state machine on constrained hardware.",
     tech=["Arduino (C/C++)", "HC-SR04 sonar", "Servo control"],
     figs=[("06-ultrasonic-tracker", "hardware_tracker.jpg",
            "The assembled tracker: an Arduino driving a dual-servo pan/tilt head and a three-sensor ultrasonic array on a custom mount.")])

proj(id="07-cpp-banking", slug="cpp-banking-system",
     num="07", title="C++ Banking System (OOP)",
     subtitle="Encapsulated accounts with MPIN authentication",
     period="Nov 2022", cats=["Software"],
     accent="#5566d6", family="code", featured=False,
     repo="https://github.com/aeroengrali/cpp-banking-system",
     overview="A console banking application built on object-oriented principles: a bankAccount "
              "class encapsulates balance and MPIN with guarded deposit, withdrawal and "
              "authenticated login. A four-person academic team project.",
     challenge="Model a small bank with safe state: balances and PINs must be protected, operations "
               "validated, and access gated behind authentication.",
     approach=["A bankAccount class encapsulates balance and MPIN (private members, accessors)",
               "Guarded deposit, withdrawal and balance enquiry with validation",
               "MPIN-authenticated login flow",
               "Supporting policy, security-awareness and terms modules"],
     flow=["Create account", "MPIN login", "Deposit / Withdraw", "Validation", "Policy + terms"],
     metrics=[("Paradigm", "Object-oriented C++"), ("Core", "bankAccount class"),
              ("Auth", "MPIN login"), ("Team", "4 students")],
     outcomes="Demonstrates object-oriented design (encapsulation, methods), input validation, "
              "simple authentication, and structured program flow in C++.",
     tech=["C++", "OOP", "Standard library"],
     note="A four-person team project, credited as such. Ali contributed the class design and core "
          "account/transaction logic.",
     figs=[("07-cpp-banking", "banking_code.png",
            "The bankAccount class: balance and MPIN encapsulated as private members, with guarded deposit, withdrawal and authenticated access.")])

proj(id="08-a320-cad", slug="a320-solidworks",
     num="08", title="Airbus A320 SolidWorks CAD",
     subtitle="Solid model with dimensioned drawings and renders",
     period="Jul 2024", cats=["CAD"],
     accent="#2bb3c0", family="cube", featured=False,
     repo="https://github.com/aeroengrali/a320-solidworks",
     overview="An A320-class airliner modelled in SolidWorks, with a dimensioned multi-view "
              "engineering blueprint and isometric renders. An independent CAD exercise from public "
              "reference dimensions, with no manufacturer data.",
     challenge="Reproduce the form of a narrow-body airliner as a clean solid model and document it "
               "with a proper engineering drawing.",
     approach=["Sketch and extrude the fuselage from a dimensioned side profile",
               "Build the wing and empennage from guided blueprints",
               "Produce a dimensioned three-view engineering drawing",
               "Render isometric and in-scene views of the finished model"],
     flow=["Reference dimensions", "Fuselage solid", "Wings + empennage", "Engineering drawing", "Renders"],
     metrics=[("Tool", "SolidWorks"), ("Output", "part + drawing + renders"),
              ("Drawing", "dimensioned 3-view"), ("Data", "public dimensions only")],
     outcomes="Demonstrates parametric solid modelling, surfacing an aircraft form, and producing a "
              "standards-style multi-view engineering drawing.",
     tech=["SolidWorks", "Engineering drawing", "Rendering"],
     note="No Airbus proprietary data is used or reproduced; the model is built from publicly "
          "available reference dimensions and carries no manufacturer markings.",
     figs=[("08-a320-cad", "A320_drawing-10.png", "Isometric and in-scene renders of the finished model."),
           ("08-a320-cad", "A320_drawing-05.png", "Dimensioned top and side blueprints used to drive the model."),
           ("08-a320-cad", "A320_drawing-11.png", "Further flight-scene renders of the A320 model.")])

proj(id="09-morphobot-fyp", slug="morphobot-digital-twin",
     num="09", title="Rover-Hover Morphobot Digital Twin",
     subtitle="Final-year project (in progress)",
     period="2025-2026", cats=["GNC & Controls", "Flight Control"],
     accent="#1f9e5a", family="gear", featured=True, repo=None,
     overview="A MATLAB/Simulink digital twin of a two-mode rover and hover transforming "
              "quadcopter whose motors sit inside its wheels. It covers flight dynamics, cascaded "
              "PID flight control, ESKF state estimation, skid-steer control and a mode-transition "
              "supervisor, paired with vendor-built hardware.",
     challenge="A vehicle that both flies and drives has two dynamics regimes and a transition "
               "between them, modelled faithfully and paired with real hardware.",
     approach=["Model the quad flight dynamics and a cascaded PID flight controller",
               "Estimate state with an Error-State Kalman Filter (ESKF)",
               "Add skid-steer control for the ground mode",
               "A mode supervisor manages the hover-to-rover transition"],
     flow=["Hover (quad)", "Mode supervisor", "Transition", "Rover (skid-steer)", "ESKF estimation"],
     metrics=[("Modes", "hover + rover"), ("Flight control", "cascaded PID"),
              ("Estimation", "ESKF"), ("Status", "in progress")],
     outcomes="A hardware-paired digital-twin workflow spanning flight dynamics, control, estimation "
              "and mode transition for a transforming robot.",
     tech=["MATLAB / Simulink", "Stateflow"],
     note="Intentionally high level. Quantitative results, parameter values and the full project "
          "report are withheld until the project is defended.",
     figs=[("09-morphobot-fyp", "contact_sheet.png", "CAD part set of the transforming quadcopter (motor-in-wheel drive, lift arms, gearboxes, wheels)."),
           ("09-morphobot-fyp", "hardware_01.jpg", "The distinctive motor-in-wheel hardware assembly."),
           ("09-morphobot-fyp", "hardware_03.jpg", "The physical build of the morphobot.")])

# ----------------------------------------------------------------- brand SVG
def _motif(family, accent):
    a = accent
    if family == "orbit":
        return (f'<g fill="none" stroke="{a}" stroke-width="2" opacity="0.5">'
                f'<ellipse cx="980" cy="180" rx="240" ry="86" transform="rotate(-20 980 180)"/>'
                f'<ellipse cx="980" cy="180" rx="160" ry="56" transform="rotate(-20 980 180)"/>'
                f'<ellipse cx="980" cy="180" rx="86" ry="30" transform="rotate(-20 980 180)"/></g>'
                f'<circle cx="980" cy="180" r="8" fill="#eaf2fb"/><circle cx="1120" cy="120" r="5" fill="{a}"/>')
    if family == "path":
        return (f'<path d="M760 470 C 880 360, 980 420, 1140 200" fill="none" stroke="{a}" stroke-width="2.5" opacity="0.8" stroke-dasharray="2 10" stroke-linecap="round"/>'
                f'<g fill="{a}" opacity="0.85"><circle cx="820" cy="426" r="5"/><circle cx="940" cy="392" r="5"/><circle cx="1060" cy="300" r="5"/></g>'
                f'<circle cx="1140" cy="200" r="9" fill="#eaf2fb"/>')
    if family == "wave":
        pts = " ".join(f"{760+i*16},{200+int(70*__import__('math').sin(i/3.2))}" for i in range(28))
        return f'<polyline points="{pts}" fill="none" stroke="{a}" stroke-width="3" opacity="0.7"/>'
    if family == "sat":
        return (f'<g stroke="{a}" stroke-width="2" fill="none" opacity="0.6"><ellipse cx="1000" cy="200" rx="220" ry="90" transform="rotate(18 1000 200)"/></g>'
                f'<g transform="translate(980,150)" fill="{a}" opacity="0.85"><rect x="-16" y="-12" width="32" height="24" rx="3"/>'
                f'<rect x="-60" y="-6" width="36" height="12" opacity="0.6"/><rect x="24" y="-6" width="36" height="12" opacity="0.6"/></g>')
    if family == "cube":
        return (f'<g fill="none" stroke="{a}" stroke-width="2" opacity="0.65" transform="translate(980,180)">'
                f'<path d="M0 -70 L70 -35 L70 45 L0 80 L-70 45 L-70 -35 Z"/>'
                f'<path d="M0 -70 L0 10 M0 10 L70 45 M0 10 L-70 45"/></g>')
    if family == "circuit":
        return (f'<g stroke="{a}" stroke-width="2" fill="none" opacity="0.6">'
                f'<path d="M820 140 H960 V260 H1110"/><path d="M820 240 H900 V160 H1110"/></g>'
                f'<g fill="{a}"><circle cx="820" cy="140" r="6"/><circle cx="820" cy="240" r="6"/><circle cx="1110" cy="260" r="6"/><circle cx="1110" cy="160" r="6"/></g>')
    if family == "code":
        return (f'<g fill="none" stroke="{a}" stroke-width="3" opacity="0.6" stroke-linecap="round">'
                f'<path d="M900 130 q-40 0 -40 50 t-40 50 q40 0 40 50 t40 50"/>'
                f'<path d="M1060 130 q40 0 40 50 t40 50 q-40 0 -40 50 t-40 50"/></g>')
    if family == "gear":
        return (f'<g fill="none" stroke="{a}" stroke-width="2.5" opacity="0.6" transform="translate(990,185)">'
                f'<circle r="58"/><circle r="22"/>'
                + "".join(f'<rect x="-6" y="-78" width="12" height="20" rx="2" transform="rotate({d})"/>' for d in range(0,360,45))
                + "</g>")
    return ""

def _wrap(s, n=24):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if len(cur)+len(w)+1 <= n: cur = (cur+" "+w).strip()
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines[:2]

def card_header_svg(p):
    a = p["accent"]; cat = p["cats"][0]
    lines = _wrap(p["title"], 28)
    ty = 290 if len(lines) == 2 else 318
    sy = ty + (len(lines)-1)*66 + 52
    title_tspans = "".join(
        f'<tspan x="70" dy="{0 if i==0 else 66}">{esc(l)}</tspan>' for i, l in enumerate(lines))
    chips = ""
    for i, t in enumerate(p["tech"][:3]):
        chips += (f'<g transform="translate({70+i*0},0)"></g>')
    chiprow = ""
    x = 70
    for t in p["tech"][:3]:
        w = 22 + len(t)*9.2
        chiprow += (f'<g transform="translate({x},520)"><rect width="{w:.0f}" height="34" rx="17" fill="#ffffff" opacity="0.08"/>'
                    f'<text x="{w/2:.0f}" y="22" text-anchor="middle" fill="#cfe0f1" font-size="15" font-family="system-ui,Segoe UI,Arial">{esc(t)}</text></g>')
        x += w + 12
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" role="img" aria-label="{esc(p['title'])}">
<defs>
<linearGradient id="bg{p['num']}" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#0c2236"/><stop offset="1" stop-color="#081320"/></linearGradient>
<radialGradient id="gl{p['num']}" cx="0.82" cy="0.22" r="0.6">
<stop offset="0" stop-color="{a}" stop-opacity="0.28"/><stop offset="1" stop-color="{a}" stop-opacity="0"/></radialGradient>
</defs>
<rect width="1200" height="630" fill="url(#bg{p['num']})"/>
<rect width="1200" height="630" fill="url(#gl{p['num']})"/>
<rect x="0" y="0" width="12" height="630" fill="{a}"/>
{_motif(p['family'], a)}
<text x="1150" y="150" text-anchor="end" font-family="system-ui,Segoe UI,Arial" font-weight="800" font-size="150" fill="#ffffff" opacity="0.05">{p['num']}</text>
<text x="70" y="120" font-family="system-ui,Segoe UI,Arial" font-weight="700" font-size="22" letter-spacing="3" fill="{a}">{esc(cat.upper())}</text>
<text x="70" y="{ty}" font-family="system-ui,Segoe UI,Arial" font-weight="800" font-size="56" fill="#ffffff">{title_tspans}</text>
<text x="70" y="{sy}" font-family="system-ui,Segoe UI,Arial" font-size="27" fill="#aac3dc">{esc(p['subtitle'])}</text>
{chiprow}
<text x="1150" y="545" text-anchor="end" font-family="system-ui,Segoe UI,Arial" font-size="20" fill="#7f9cb6">{esc(p['period'])}</text>
</svg>'''

def diagram_svg(p):
    a = p["accent"]; stages = p["flow"]
    n = len(stages); W = 1100; gap = 26
    bw = (W - gap*(n-1)) / n
    boxes = ""
    for i, s in enumerate(stages):
        x = i*(bw+gap)
        words = _wrap(s, 14)
        tsp = "".join(f'<tspan x="{x+bw/2:.0f}" dy="{0 if j==0 else 18}">{esc(w)}</tspan>' for j,w in enumerate(words))
        cy = 60 - (len(words)-1)*9
        boxes += (f'<g><rect x="{x:.0f}" y="20" width="{bw:.0f}" height="84" rx="12" fill="#f4f8fc" stroke="{a}" stroke-width="2"/>'
                  f'<text x="{x+bw/2:.0f}" y="{cy}" text-anchor="middle" font-family="system-ui,Segoe UI,Arial" font-weight="600" font-size="16" fill="#15324a">{tsp}</text></g>')
        if i < n-1:
            ax = x+bw; boxes += (f'<path d="M{ax+4:.0f} 62 L{ax+gap-4:.0f} 62" stroke="{a}" stroke-width="3" marker-end="url(#ah{p["num"]})"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 124" role="img" aria-label="Pipeline: {esc(' to '.join(stages))}">
<defs><marker id="ah{p['num']}" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 Z" fill="{a}"/></marker></defs>
{boxes}</svg>'''

def favicon_svg():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
            '<rect width="64" height="64" rx="14" fill="#0c2236"/>'
            '<ellipse cx="32" cy="32" rx="22" ry="9" fill="none" stroke="#2f7fd1" stroke-width="3" transform="rotate(-25 32 32)"/>'
            '<text x="32" y="41" text-anchor="middle" font-family="system-ui,Arial" font-weight="800" font-size="26" fill="#ffffff">A</text></svg>')

def og_svg():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630">
<defs><linearGradient id="ob" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0c2236"/><stop offset="1" stop-color="#06101b"/></linearGradient>
<radialGradient id="og" cx="0.8" cy="0.25" r="0.7"><stop offset="0" stop-color="#2f7fd1" stop-opacity="0.3"/><stop offset="1" stop-color="#2f7fd1" stop-opacity="0"/></radialGradient></defs>
<rect width="1200" height="630" fill="url(#ob)"/><rect width="1200" height="630" fill="url(#og)"/>
<g fill="none" stroke="#2f7fd1" stroke-width="2" opacity="0.5">
<ellipse cx="950" cy="200" rx="300" ry="110" transform="rotate(-20 950 200)"/>
<ellipse cx="950" cy="200" rx="200" ry="72" transform="rotate(-20 950 200)"/></g>
<circle cx="950" cy="200" r="9" fill="#eaf2fb"/>
<text x="80" y="250" font-family="system-ui,Segoe UI,Arial" font-weight="800" font-size="84" fill="#ffffff">Ali Murtaza</text>
<text x="80" y="312" font-family="system-ui,Segoe UI,Arial" font-weight="700" font-size="32" fill="#7fb6e6">Aerospace Engineering (Guidance, Navigation &amp; Control)</text>
<text x="80" y="380" font-family="system-ui,Segoe UI,Arial" font-size="27" fill="#aac3dc">Flight control, state estimation, navigation, spacecraft, CAD.</text>
<text x="80" y="556" font-family="system-ui,Segoe UI,Arial" font-weight="700" font-size="24" fill="#cfe0f1">aeroengrali.github.io</text>
</svg>'''

# ----------------------------------------------------------------- assembly
def copy_assets():
    if os.path.exists(APROOT): shutil.rmtree(APROOT)
    for p in P:
        dst = os.path.join(APROOT, p["slug"]); os.makedirs(dst, exist_ok=True)
        with open(os.path.join(dst, "header.svg"), "w", encoding="utf-8") as f: f.write(card_header_svg(p))
        with open(os.path.join(dst, "diagram.svg"), "w", encoding="utf-8") as f: f.write(diagram_svg(p))
        for pid, fn, _cap in p["figs"]:
            srcdir = os.path.join(PROJ, pid, "assets"); found = None
            for base, _d, files in os.walk(srcdir):
                if fn in files: found = os.path.join(base, fn); break
            if found: shutil.copy2(found, os.path.join(dst, fn))
            else: print("  MISSING fig:", p["slug"], fn)
        if p["slug"] == "quadcopter-attitude-control":
            for base, _d, files in os.walk(os.path.join(PROJ, p["id"], "assets")):
                if "attitude_trajectory.csv" in files:
                    shutil.copy2(os.path.join(base, "attitude_trajectory.csv"), os.path.join(dst, "attitude_trajectory.csv"))
    with open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8") as f: f.write(favicon_svg())
    with open(os.path.join(OUT, "og.svg"), "w", encoding="utf-8") as f: f.write(og_svg())

def head(title, desc, depth=0, og_img="og.png", page_url=SITE["url"]):
    up = "../" * depth
    return f'''<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="icon" href="{up}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{up}icon-180.png">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{esc(page_url)}">
<meta property="og:image" content="{SITE['url']}/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="stylesheet" href="{up}style.css">
</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="wrap navin">
<a class="brand" href="{up}index.html">Ali&nbsp;Murtaza</a>
<nav aria-label="Primary"><a href="{up}index.html#projects">Projects</a><a href="{up}index.html#skills">Skills</a><a href="{up}index.html#about">About</a><a href="{up}index.html#contact">Contact</a></nav>
</div></header>'''

def foot(script=""):
    return f'''<footer class="foot" id="contact"><div class="wrap">
<h2>Get in touch</h2>
<p>Open to GNC, flight-control, simulation and aerospace R&amp;D roles, internships and graduate study.</p>
<p class="links">
<a href="mailto:{SITE['email']}">{SITE['email']}</a> &middot;
<a href="{SITE['github']}" rel="noopener">GitHub</a> &middot;
<a href="{SITE['linkedin']}" rel="noopener">LinkedIn</a> &middot;
<span>{esc(SITE['location'])}</span></p>
<p class="fine">© 2026 Ali Murtaza &middot; {esc(SITE['grad'])}</p>
</div></footer>{script}</body></html>'''

def card(p):
    tags = "".join(f'<span class="tag">{esc(c)}</span>' for c in p["cats"][:2])
    feat = '<span class="badge">Featured</span>' if p.get("featured") else ""
    return f'''<a class="card" href="projects/{p['slug']}.html" data-cats="{esc(' '.join(p['cats']))}">
<div class="card-img"><img loading="lazy" width="1200" height="630" src="assets/projects/{p['slug']}/header.svg" alt="{esc(p['title'])} cover"></div>
<div class="card-body"><div class="card-top">{feat}<span class="period">{esc(p['period'])}</span></div>
<h3>{esc(p['title'])}</h3><p class="sub">{esc(p['subtitle'])}</p>
<div class="tags">{tags}</div><span class="card-cta">View project &rarr;</span></div></a>'''

HERO_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" preserveAspectRatio="xMidYMid slice">
<defs><radialGradient id="hg" cx="72%" cy="28%" r="85%"><stop offset="0%" stop-color="#1b4a73"/><stop offset="100%" stop-color="#071421"/></radialGradient></defs>
<rect width="1200" height="420" fill="url(#hg)"/>
<g fill="none" stroke="#3b82c4" stroke-width="1.4" opacity="0.5">
<ellipse cx="880" cy="150" rx="330" ry="120" transform="rotate(-18 880 150)"/>
<ellipse cx="880" cy="150" rx="230" ry="80" transform="rotate(-18 880 150)"/>
<ellipse cx="880" cy="150" rx="135" ry="46" transform="rotate(-18 880 150)"/></g>
<path d="M40 380 C 320 320, 520 270, 790 120" fill="none" stroke="#5fa8e0" stroke-width="2" opacity="0.7"/>
<circle cx="790" cy="120" r="6" fill="#9cc3e6"/><circle cx="880" cy="150" r="9" fill="#e8f1fb"/>
<g fill="#6fb0e6" opacity="0.55"><circle cx="180" cy="80" r="2"/><circle cx="320" cy="180" r="2"/><circle cx="120" cy="250" r="2"/><circle cx="520" cy="90" r="2"/><circle cx="1050" cy="300" r="2"/></g>
</svg>'''

def build_index():
    cats = ["All", "GNC & Controls", "Estimation & Navigation", "Flight Control",
            "Flight Dynamics", "Spacecraft", "Software", "Embedded", "CAD"]
    chips = "".join(f'<button class="chip{" on" if c=="All" else ""}" data-filter="{esc(c)}" aria-pressed="{"true" if c=="All" else "false"}">{esc(c)}</button>' for c in cats)
    cards = "\n".join(card(p) for p in P)
    skills = ""
    for grp, items in SKILLS:
        lis = "".join(f"<li>{esc(i)}</li>" for i in items)
        skills += f'<div class="skill"><h3>{esc(grp)}</h3><ul>{lis}</ul></div>'
    doc = head(f"{SITE['name']} | {SITE['role']}", SITE["tagline"])
    doc += f'''
<main id="main">
<section class="hero"><div class="hero-svg" aria-hidden="true">{HERO_SVG}</div><div class="wrap">
<p class="eyebrow">{esc(SITE['role'])}</p>
<h1>{esc(SITE['name'])}</h1>
<p class="lede">{esc(SITE['tagline'])}</p>
<p class="hero-meta">{esc(SITE['grad'])}</p>
<div class="cta"><a class="btn" href="#projects">View projects</a>
<a class="btn ghost" href="{SITE['github']}" rel="noopener">GitHub</a></div>
<div class="stats"><div><b>9</b><span>projects</span></div><div><b>MATLAB &amp; C++</b><span>simulation &amp; code</span></div><div><b>GNC</b><span>focus area</span></div></div>
</div></section>

<section id="projects" class="sec"><div class="wrap">
<h2>Projects</h2>
<p class="sec-lede">Flight control, state estimation, navigation, flight dynamics, spacecraft attitude control, software and CAD. Each card opens a full write-up with the approach, results and figures.</p>
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
    doc += foot('<script src="app.js"></script>')
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f: f.write(doc)

def build_project(p):
    page_url = f"{SITE['url']}/projects/{p['slug']}.html"
    doc = head(f"{p['title']} | {SITE['name']}", p["overview"][:155], depth=1,
               og_img=f"assets/projects/{p['slug']}/header.svg".replace(".svg",".svg"), page_url=page_url)
    # use the project header svg as OG (svg ok for og:image fallback; png master also set on home)
    approach = "".join(f"<li>{esc(a)}</li>" for a in p["approach"])
    metrics = "".join(f"<tr><td>{esc(l)}</td><td>{esc(v)}</td></tr>" for l, v in p["metrics"])
    figs = ""
    for pid, fn, cap in p["figs"]:
        figs += f'<figure><img loading="lazy" src="../assets/projects/{p["slug"]}/{fn}" alt="{esc(cap)}"><figcaption>{esc(cap)}</figcaption></figure>'
    figblock = f'<section class="psec"><h2>Results</h2><div class="metricwrap"><table class="metrics"><tbody>{metrics}</tbody></table></div><div class="gallery">{figs}</div></section>' if figs else \
               f'<section class="psec"><h2>Results</h2><div class="metricwrap"><table class="metrics"><tbody>{metrics}</tbody></table></div></section>'
    demo = ""
    if p.get("demo"):
        demo = f'<section class="psec"><h2>Interactive 3D</h2><iframe class="demo" src="../{p["demo"]}" title="Interactive 3D attitude viewer" loading="lazy"></iframe></section>'
    note = f'<p class="note">{esc(p["note"])}</p>' if p.get("note") else ""
    links = ""
    if p.get("repo"): links += f'<a class="btn" href="{esc(p["repo"])}" rel="noopener">Source on GitHub &rarr;</a>'
    if p.get("demo"): links += f'<a class="btn ghost" href="../{p["demo"]}">Open 3D demo</a>'
    cta_html = f'<div class="cta">{links}</div>' if links else ''
    tags = "".join(f'<span class="tag alt">{esc(c)}</span>' for c in p["cats"])
    tech = "".join(f'<span class="tag">{esc(t)}</span>' for t in p["tech"])
    doc += f'''
<main id="main" class="proj"><div class="wrap">
<p class="crumb"><a href="../index.html#projects">&larr; All projects</a></p>
<div class="pbanner"><img src="../assets/projects/{p['slug']}/header.svg" alt="{esc(p['title'])} cover" width="1200" height="630"></div>
<h1>{esc(p['title'])}</h1>
<p class="lede">{esc(p['subtitle'])}</p>
<div class="tags">{tags} <span class="period">{esc(p['period'])}</span></div>
{note}

<section class="psec"><h2>Overview</h2><p class="overview">{esc(p['overview'])}</p></section>
<section class="psec"><h2>The challenge</h2><p>{esc(p['challenge'])}</p></section>
<section class="psec"><h2>Approach</h2>
<div class="diagram"><img src="../assets/projects/{p['slug']}/diagram.svg" alt="Pipeline diagram for {esc(p['title'])}"></div>
<ul class="approach">{approach}</ul></section>
{figblock}
{demo}
<section class="psec"><h2>What it demonstrates</h2><p>{esc(p['outcomes'])}</p></section>
<section class="psec"><h2>Built with</h2><div class="tags">{tech}</div>
{cta_html}</section>
</div></main>
'''
    doc += foot()
    with open(os.path.join(OUT, "projects", f'{p["slug"]}.html'), "w", encoding="utf-8") as f: f.write(doc)

def build_demo():
    src = '''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Quadcopter attitude (3D demo)</title>
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta property="og:title" content="Quadcopter Attitude Control - Interactive 3D Demo">
<meta property="og:image" content="https://aeroengrali.github.io/og.png">
<meta name="twitter:card" content="summary_large_image">
<style>html,body{margin:0;height:100%;background:#0b1f33;color:#cfe2f5;font:14px system-ui;overflow:hidden}
#hud{position:fixed;left:12px;top:10px;background:rgba(8,21,34,.7);padding:8px 12px;border-radius:8px;line-height:1.5}
#hud b{color:#fff}.sr{position:absolute;left:-9999px}</style></head><body>
<h1 class="sr">Quadcopter Attitude Control: Interactive 3D Demo</h1>
<div id="hud">Quadcopter attitude (simulated)<br><span id="t">t = 0.0 s</span> &middot; <span id="rpy">roll 0 pitch 0 yaw 0</span><br><span style="opacity:.7">drag to orbit &middot; loops automatically</span></div>
<script type="module">
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';
import {OrbitControls} from 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/controls/OrbitControls.js';
const scene=new THREE.Scene(); scene.background=new THREE.Color(0x0b1f33);
const cam=new THREE.PerspectiveCamera(50,innerWidth/innerHeight,0.1,100); cam.position.set(3.2,2.4,3.6);
const rnd=new THREE.WebGLRenderer({antialias:true}); rnd.setSize(innerWidth,innerHeight); rnd.setPixelRatio(Math.min(devicePixelRatio,2)); document.body.appendChild(rnd.domElement);
const ctr=new OrbitControls(cam,rnd.domElement); ctr.enableDamping=true; ctr.enablePan=false;
scene.add(new THREE.AmbientLight(0xffffff,0.7)); const d=new THREE.DirectionalLight(0xffffff,1.1); d.position.set(5,8,4); scene.add(d);
scene.add(new THREE.GridHelper(12,12,0x274a66,0x18324a)); scene.add(new THREE.AxesHelper(1.6));
const quad=new THREE.Group();
const bodyMat=new THREE.MeshStandardMaterial({color:0x2c3e50,metalness:.3,roughness:.5});
const armMat=new THREE.MeshStandardMaterial({color:0x34495e});
const rotorMat=[0xd92a2a,0x1a73b8,0x2aa14e,0xeab308].map(c=>new THREE.MeshStandardMaterial({color:c}));
quad.add(new THREE.Mesh(new THREE.BoxGeometry(0.5,0.16,0.5),bodyMat));
const L=1.0,pos=[[L,L],[-L,L],[-L,-L],[L,-L]];
pos.forEach((p,i)=>{const a=new THREE.Mesh(new THREE.BoxGeometry(0.07,0.05,1.4),armMat);
 a.position.set(p[0]/2,0,p[1]/2); a.lookAt(0,0,0); quad.add(a);
 const r=new THREE.Mesh(new THREE.CylinderGeometry(0.34,0.34,0.03,28),rotorMat[i]);
 r.position.set(p[0],0.09,p[1]); r.userData.spin=true; quad.add(r);});
scene.add(quad);
let traj=[[0,0,0,0]];
fetch('assets/projects/quadcopter-attitude-control/attitude_trajectory.csv').then(r=>r.text()).then(t=>{
 traj=t.trim().split(/\\r?\\n/).map(l=>l.split(',').map(Number)).filter(a=>a.length>=4&&!isNaN(a[0]));}).catch(()=>{});
const tEl=document.getElementById('t'),rpyEl=document.getElementById('rpy');
let k=0,last=performance.now(),acc=0;
function frame(now){requestAnimationFrame(frame);
 acc+=(now-last)/1000; last=now;
 if(traj.length>1){ if(acc>0.04){acc=0;k=(k+1)%traj.length;}
  const [tt,roll,pitch,yaw]=traj[k];
  quad.rotation.set(THREE.MathUtils.degToRad(roll),THREE.MathUtils.degToRad(yaw),THREE.MathUtils.degToRad(pitch),'XYZ');
  tEl.textContent='t = '+tt.toFixed(1)+' s';
  rpyEl.textContent=`roll ${roll.toFixed(0)} pitch ${pitch.toFixed(0)} yaw ${yaw.toFixed(0)}`;}
 quad.children.forEach(c=>{if(c.userData.spin)c.rotation.y+=0.4;});
 ctr.update(); rnd.render(scene,cam);}
requestAnimationFrame(frame);
addEventListener('resize',()=>{cam.aspect=innerWidth/innerHeight;cam.updateProjectionMatrix();rnd.setSize(innerWidth,innerHeight);});
</script></body></html>'''
    with open(os.path.join(OUT, "quad-demo.html"), "w", encoding="utf-8") as f: f.write(src)

if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "projects"), exist_ok=True)
    copy_assets(); build_index()
    for p in P: build_project(p)
    build_demo()
    print("Site v2 generated:", len(P), "projects + index + demo")

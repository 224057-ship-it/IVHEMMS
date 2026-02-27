import os

base_dir = r"c:\Users\Mega Tech\Desktop\Madlin1\vms-frontend"

profiles = [
    {
        "role": "admin",
        "dir": "admin",
        "title": "Admin",
        "name": "Admin User",
        "avatar_bg": "4361ee",
        "sidebar_head": """        <div class="brand">
            <i class="bi bi-car-front-fill text-primary"></i> VMS Portal
        </div>
        <div class="sidebar-heading">Core</div>
        <ul class="sidebar-menu">
            <li><a href="../dashboards/admin.html"><i class="bi bi-grid-1x2-fill"></i> Admin Dash</a></li>
            <li><a href="../dashboards/client.html"><i class="bi bi-person-badge"></i> Client Dash</a></li>
            <li><a href="../dashboards/technician.html"><i class="bi bi-tools"></i> Tech Dash</a></li>
        </ul>
        <div class="sidebar-heading">Modules</div>
        <ul class="sidebar-menu">
            <li><a href="../client/book-appointment.html"><i class="bi bi-calendar-check"></i> Appointments</a></li>
            <li><a href="../technician/work-orders.html"><i class="bi bi-card-checklist"></i> Work Orders</a></li>
            <li><a href="../inventory/stock-list.html"><i class="bi bi-box-seam"></i> Inventory</a></li>
            <li><a href="../finance/invoice-list.html"><i class="bi bi-receipt"></i> Finance</a></li>
            <li><a href="../analytics/vehicle-health.html"><i class="bi bi-graph-up-arrow"></i> Analytics</a></li>
        </ul>""",
        "subtitle": "System Administrator",
        "fields": [
            ("Role Badge", "bi-shield-fill-check", "text", "Super Admin", True)
        ]
    },
    {
        "role": "service-manager",
        "dir": "service-manager",
        "title": "Service Manager",
        "name": "Sarah Manager",
        "avatar_bg": "7209b7",
        "sidebar_head": """        <div class="brand">
            <i class="bi bi-diagram-3-fill text-primary"></i> VMS Service
        </div>
        <div class="sidebar-heading">Management</div>
        <ul class="sidebar-menu">
            <li><a href="../dashboards/service-manager.html"><i class="bi bi-grid-1x2-fill"></i> Manager Dash</a></li>
            <li><a href="../technician/work-orders.html"><i class="bi bi-files"></i> All Work Orders</a></li>
            <li><a href="../client/book-appointment.html"><i class="bi bi-calendar-range"></i> Schedule</a></li>
            <li><a href="#"><i class="bi bi-people"></i> Technicians</a></li>
        </ul>""",
        "subtitle": "Service Dept Head",
        "fields": [
            ("Department", "bi-building", "text", "Service & Repair", False),
            ("Assigned Branch", "bi-geo-alt", "text", "Downtown Main Branch", False)
        ]
    },
    {
        "role": "general-manager",
        "dir": "general-manager",
        "title": "General Manager",
        "name": "General Manager",
        "avatar_bg": "2b2d42",
        "sidebar_head": """        <div class="brand">
            <i class="bi bi-briefcase-fill text-primary"></i> VMS Corp
        </div>
        <div class="sidebar-heading">Executive</div>
        <ul class="sidebar-menu">
            <li><a href="../dashboards/general-manager.html"><i class="bi bi-pie-chart-fill"></i> Exec Dash</a></li>
            <li><a href="../analytics/vehicle-health.html"><i class="bi bi-graph-up"></i> Reports</a></li>
            <li><a href="#"><i class="bi bi-building"></i> Branches</a></li>
            <li><a href="#"><i class="bi bi-gear"></i> Settings</a></li>
        </ul>""",
        "subtitle": "Executive GM",
        "fields": [
            ("Office Location", "bi-geo-alt", "text", "HQ - Executive Floor", False)
        ]
    },
    {
        "role": "stock-keeper",
        "dir": "stock-keeper",
        "title": "Stock Keeper",
        "name": "Warehouse Keeper",
        "avatar_bg": "ffb703",
        "sidebar_head": """        <div class="brand">
            <i class="bi bi-box-seam-fill text-primary"></i> VMS Inventory
        </div>
        <div class="sidebar-heading">Inventory</div>
        <ul class="sidebar-menu">
            <li><a href="../dashboards/stock-keeper.html"><i class="bi bi-inboxes-fill"></i> Dashboard</a></li>
            <li><a href="../inventory/stock-list.html"><i class="bi bi-list-ul"></i> Stock List</a></li>
            <li><a href="../inventory/update-stock.html"><i class="bi bi-arrow-repeat"></i> Update Stock</a></li>
            <li><a href="../inventory/low-stock.html"><i class="bi bi-exclamation-triangle"></i> Low Stock Alerts</a></li>
        </ul>""",
        "subtitle": "Inventory Manager",
        "fields": [
            ("Warehouse Location", "bi-geo-alt", "text", "Warehouse A (Downtown)", False)
        ]
    },
    {
        "role": "finance",
        "dir": "finance",
        "title": "Finance Manager",
        "name": "Finance Manager",
        "avatar_bg": "06d6a0",
        "sidebar_head": """        <div class="brand">
            <i class="bi bi-cash-stack text-primary"></i> VMS Finance
        </div>
        <div class="sidebar-heading">Accounting</div>
        <ul class="sidebar-menu">
            <li><a href="../dashboards/finance-manager.html"><i class="bi bi-wallet2"></i> Dashboard</a></li>
            <li><a href="../finance/invoice-list.html"><i class="bi bi-receipt"></i> Invoices</a></li>
            <li><a href="../finance/create-invoice.html"><i class="bi bi-plus-circle"></i> Create Invoice</a></li>
            <li><a href="../finance/financial-report.html"><i class="bi bi-file-earmark-bar-graph"></i> Reports</a></li>
        </ul>""",
        "subtitle": "Accounting & Finance",
        "fields": [
            ("Finance Department", "bi-building", "text", "Corporate Finance", False)
        ]
    },
    {
        "role": "analytics",
        "dir": "analytics",
        "title": "Data Analyst",
        "name": "Analytics Pro",
        "avatar_bg": "f72585",
        "sidebar_head": """        <div class="brand">
            <i class="bi bi-graph-up-arrow text-primary"></i> VMS Analytics
        </div>
        <div class="sidebar-heading">Data & Analytics</div>
        <ul class="sidebar-menu">
            <li><a href="../dashboards/data-analyst.html"><i class="bi bi-clipboard-data"></i> Dashboard</a></li>
            <li><a href="../analytics/vehicle-health.html"><i class="bi bi-heart-pulse"></i> Vehicle Health</a></li>
            <li><a href="../analytics/obd-data.html"><i class="bi bi-usb-drive"></i> OBD Data</a></li>
            <li><a href="../analytics/certification-report.html"><i class="bi bi-patch-check"></i> Emissions</a></li>
        </ul>""",
        "subtitle": "Data Science",
        "fields": [
            ("Analytics Role", "bi-bar-chart", "text", "Senior Data Analyst", False)
        ]
    }
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VMS - {title} Profile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <nav class="sidebar">
{sidebar_head}
    </nav>
    <main class="main-content">
        <header class="topbar">
            <div class="d-flex align-items-center gap-3">
                <button id="sidebarToggle" class="btn btn-outline-secondary d-md-none"><i class="bi bi-list"></i></button>
                <h5 class="mb-0 fw-bold d-none d-md-block">{title} Profile</h5>
            </div>
            <div class="d-flex align-items-center gap-3">
                <button id="themeSwitch" class="btn btn-outline-primary rounded-circle"><i class="bi bi-moon-stars"></i></button>
                <div class="dropdown">
                    <a href="#" class="d-flex align-items-center text-decoration-none dropdown-toggle user-profile" data-bs-toggle="dropdown">
                        <img src="https://ui-avatars.com/api/?name={avatar_name}&background={avatar_bg}&color=fff" alt="User" id="topbarAvatar">
                        <span class="ms-2 d-none d-md-inline text-body fw-semibold">{name}</span>
                    </a>
                    <ul class="dropdown-menu dropdown-menu-end shadow border-0" style="min-width: 200px;">
                        <li><a class="dropdown-item py-2" href="../{dir}/profile.html"><i class="bi bi-person me-2 text-primary"></i> View Profile</a></li>
                        <li><a class="dropdown-item py-2" href="../{dir}/profile.html#edit"><i class="bi bi-pencil-square me-2 text-info"></i> Edit Profile</a></li>
                        <li><a class="dropdown-item py-2" href="../{dir}/profile.html#security"><i class="bi bi-shield-lock me-2 text-warning"></i> Change Password</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item py-2 text-danger" href="../auth/login.html"><i class="bi bi-box-arrow-right me-2"></i> Logout</a></li>
                    </ul>
                </div>
            </div>
        </header>

        <div class="container-fluid p-4 fade-in">
            <div class="row g-4">
                <div class="col-12 col-xl-4">
                    <div class="card border-0 shadow-sm rounded-4 p-4 glass-card text-center profile-card">
                        <h5 class="fw-bold mb-4 text-start">Profile Picture</h5>
                        <div class="position-relative d-inline-block mb-3">
                            <img src="https://ui-avatars.com/api/?name={avatar_name}&background={avatar_bg}&color=fff&size=150" alt="Profile" id="profilePreview" class="rounded-circle profile-avatar border border-4 border-light shadow-sm" style="width: 150px; height: 150px; object-fit: cover;">
                            <label for="avatarUpload" class="btn btn-primary rounded-circle position-absolute bottom-0 end-0 shadow-sm edit-avatar-btn" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; cursor: pointer;">
                                <i class="bi bi-camera-fill"></i>
                            </label>
                            <input type="file" id="avatarUpload" class="d-none" accept="image/*">
                        </div>
                        <h5 class="fw-bold mb-1">{name}</h5>
                        <p class="text-muted small mb-0">{subtitle}</p>
                        <hr class="my-4 almost-invisible">
                        <div class="d-flex justify-content-center gap-3">
                            <button class="btn btn-outline-danger btn-sm px-3 rounded-pill" id="removeAvatarBtn">Remove</button>
                            <button class="btn btn-primary btn-sm px-3 rounded-pill btn-glow" id="saveAvatarBtn">Save Image</button>
                        </div>
                    </div>
                </div>

                <div class="col-12 col-xl-8">
                    <div class="row g-4 d-flex flex-column">
                        <div class="col-12" id="edit">
                            <div class="card border-0 shadow-sm rounded-4 p-4 glass-card">
                                <form id="profileForm">
                                    <div class="d-flex justify-content-between align-items-center mb-4">
                                        <h5 class="fw-bold mb-0">Personal Information</h5>
                                    </div>
                                    <div class="row g-3">
                                        <div class="col-md-6">
                                            <label class="form-label small text-muted fw-semibold uppercase-label">Full Name</label>
                                            <div class="input-group">
                                                <span class="input-group-text bg-transparent border-end-0"><i class="bi bi-person text-muted"></i></span>
                                                <input type="text" class="form-control border-start-0 ps-0 text-body bg-transparent" value="{name}" required>
                                            </div>
                                        </div>
                                        <div class="col-md-6">
                                            <label class="form-label small text-muted fw-semibold uppercase-label">Email Address</label>
                                            <div class="input-group">
                                                <span class="input-group-text bg-transparent border-end-0"><i class="bi bi-envelope text-muted"></i></span>
                                                <input type="email" class="form-control border-start-0 ps-0 text-body bg-transparent" value="{email}" required>
                                            </div>
                                        </div>
                                        <div class="col-md-6">
                                            <label class="form-label small text-muted fw-semibold uppercase-label">Phone Number</label>
                                            <div class="input-group">
                                                <span class="input-group-text bg-transparent border-end-0"><i class="bi bi-telephone text-muted"></i></span>
                                                <input type="tel" class="form-control border-start-0 ps-0 text-body bg-transparent" value="+1 (555) 987-1234">
                                            </div>
                                        </div>
{custom_fields}
                                    </div>
                                    <div class="d-flex justify-content-end mt-4">
                                        <button type="submit" class="btn btn-primary px-4 rounded-pill btn-glow">Save Changes</button>
                                    </div>
                                </form>
                            </div>
                        </div>

                        <div class="col-12" id="security">
                            <div class="card border-0 shadow-sm rounded-4 p-4 glass-card">
                                <form id="passwordForm">
                                    <h5 class="fw-bold mb-4">Security Settings</h5>
                                    <div class="row g-3">
                                        <div class="col-md-4">
                                            <label class="form-label small text-muted fw-semibold uppercase-label">Current Password</label>
                                            <div class="input-group mb-3">
                                                <span class="input-group-text bg-transparent border-end-0"><i class="bi bi-lock text-muted"></i></span>
                                                <input type="password" class="form-control border-start-0 ps-0 text-body bg-transparent" placeholder="Enter current password" required>
                                            </div>
                                        </div>
                                        <div class="col-md-4">
                                            <label class="form-label small text-muted fw-semibold uppercase-label">New Password</label>
                                            <div class="input-group mb-3">
                                                <span class="input-group-text bg-transparent border-end-0"><i class="bi bi-key text-muted"></i></span>
                                                <input type="password" class="form-control border-start-0 ps-0 text-body bg-transparent" placeholder="Enter new password" required>
                                            </div>
                                        </div>
                                        <div class="col-md-4">
                                            <label class="form-label small text-muted fw-semibold uppercase-label">Confirm Password</label>
                                            <div class="input-group mb-3">
                                                <span class="input-group-text bg-transparent border-end-0"><i class="bi bi-shield-check text-muted"></i></span>
                                                <input type="password" class="form-control border-start-0 ps-0 text-body bg-transparent" placeholder="Confirm new password" required>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="d-flex justify-content-end mt-2">
                                        <button type="submit" class="btn btn-dark px-4 rounded-pill btn-glow-dark">Update Password</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="position-fixed bottom-0 end-0 p-3" style="z-index: 10000; margin-bottom: 80px;">
            <div id="vmsToast" class="toast custom-toast align-items-center border-0 shadow-lg" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="d-flex">
                    <div class="toast-body d-flex align-items-center gap-2 fw-semibold" id="toastMessage">
                        <i class="bi bi-check-circle-fill text-success fs-5"></i>
                        <span>Changes saved successfully.</span>
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        </div>

    </main>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="../js/main.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const toastEl = document.getElementById('vmsToast');
            const bsToast = new bootstrap.Toast(toastEl, {{ delay: 3000 }});

            function showToast(message, isError = false) {{
                const toastMsg = document.getElementById('toastMessage');
                if (isError) {{
                    toastEl.classList.add('bg-danger', 'text-white');
                    toastEl.classList.remove('bg-white', 'text-body', 'glass-toast');
                    toastMsg.innerHTML = `<i class="bi bi-exclamation-triangle-fill text-white fs-5"></i> <span>${{message}}</span>`;
                }} else {{
                    toastEl.classList.remove('bg-danger', 'text-white');
                    toastEl.classList.add('glass-toast');
                    toastMsg.innerHTML = `<i class="bi bi-check-circle-fill text-success fs-5"></i> <span>${{message}}</span>`;
                }}
                bsToast.show();
            }}

            document.getElementById('profileForm').addEventListener('submit', (e) => {{
                e.preventDefault();
                showToast('Personal information updated successfully!');
            }});

            document.getElementById('passwordForm').addEventListener('submit', (e) => {{
                e.preventDefault();
                showToast('Password changed successfully!');
                e.target.reset();
            }});

            const avatarUpload = document.getElementById('avatarUpload');
            const profilePreview = document.getElementById('profilePreview');
            const topbarAvatar = document.getElementById('topbarAvatar');
            const saveAvatarBtn = document.getElementById('saveAvatarBtn');
            const removeAvatarBtn = document.getElementById('removeAvatarBtn');

            let currentAvatarUrl = profilePreview.src;
            const defaultAvatarUrl = 'https://ui-avatars.com/api/?name={avatar_name}&background={avatar_bg}&color=fff&size=150';

            avatarUpload.addEventListener('change', (e) => {{
                if (e.target.files && e.target.files[0]) {{
                    const reader = new FileReader();
                    reader.onload = (e) => {{
                        profilePreview.src = e.target.result;
                    }}
                    reader.readAsDataURL(e.target.files[0]);
                }}
            }});

            saveAvatarBtn.addEventListener('click', () => {{
                currentAvatarUrl = profilePreview.src;
                topbarAvatar.src = currentAvatarUrl;
                showToast('Profile picture saved successfully!');
            }});

            removeAvatarBtn.addEventListener('click', () => {{
                profilePreview.src = defaultAvatarUrl;
                currentAvatarUrl = defaultAvatarUrl;
                topbarAvatar.src = defaultAvatarUrl;
                showToast('Profile picture removed.');
            }});
        }});
    </script>
</body>
</html>"""

def build_custom_fields(fields):
    html = ""
    for idx, f in enumerate(fields):
        label, icon, type_, val, readonly = f
        ro = " readonly" if readonly else ""
        html += f'''                                        <div class="col-md-6">
                                            <label class="form-label small text-muted fw-semibold uppercase-label">{label}</label>
                                            <div class="input-group">
                                                <span class="input-group-text bg-transparent border-end-0"><i class="bi {icon} text-muted"></i></span>
                                                <input type="{type_}" class="form-control border-start-0 ps-0 text-body bg-transparent" value="{val}"{ro}>
                                            </div>
                                        </div>\n'''
    return html.rstrip()

for p in profiles:
    dir_path = os.path.join(base_dir, p['dir'])
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, 'profile.html')
    
    avatar_name = p['name'].replace(" ", "+")
    email = p['name'].split()[0].lower() + "@vms.com"
    
    custom_fields_html = build_custom_fields(p['fields'])
    
    final_html = template.format(
        title=p['title'],
        sidebar_head=p['sidebar_head'],
        avatar_name=avatar_name,
        avatar_bg=p['avatar_bg'],
        name=p['name'],
        dir=p['dir'],
        subtitle=p['subtitle'],
        email=email,
        custom_fields=custom_fields_html
    )
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"Generated {file_path}")

print("Profiles generation complete.")

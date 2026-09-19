# Raw user records: (User ID, Name, Role, Is_Active, Login_Attempts) 
users = [ (101, "Alice", "admin", True, 1),  
(102, "Bob", "member", True, 4),  
(103, "Charlie", "editor", False, 0),  
(104, "Diana", "admin", False, 6), 
(105, "Evan", "member", True, 2),  
(106, "Fiona", "guest", True, 0), ] 

# print(dir(list))
# if users == True and users =="admin":
active_granted_count = 0
inactive_count = 0
security_alert_count = 0

for user_id, name, role, is_active, login_attempts in users:
    
#login attempts
    if login_attempts >= 5:
        print(f"[ALERT] Account {name} is LOCKED due to excessive failed logins ({login_attempts} attempts).")
        security_alert_count += 1

    if is_active and role == "admin":
        print(f"[GRANT] Full system access granted to {name} (ID: {user_id})")
        active_granted_count += 1
    elif is_active and role in ("member", "editor"):
        print(f"[GRANT] Standard access granted to {name} (ID: {user_id})")
        active_granted_count += 1
    elif not is_active:
        print(f"[DENIED] Account {name} is inactive.")
        inactive_count += 1
    # {"role" : "admin","is_active": True }
print( "[GRANT] Full system access granted to <Name> (ID: <ID>)")



print("\n====================================")
print("AUDIT SUMMARY REPORT")
print("====================================")
print(f"Total Active Users Granted: {active_granted_count}")
print(f"Total Inactive Accounts: {inactive_count}")
print(f"Total Security Alerts: {security_alert_count}")
print("====================================")
ticket_ids = [101, 102, 103, 104]
statuses = ["open", "closed", "open", "open"]
priorities = ["low", "high", "high", "medium"]

dits_ticket = {x: y for x,y in zip(ticket_ids, statuses)}
ticket_high = []
for ticket,status,priority in zip(ticket_ids, statuses, priorities):
    if status == "open" and priority == "high":
        ticket_high.append(ticket)
print(dits_ticket)
print(ticket_high)

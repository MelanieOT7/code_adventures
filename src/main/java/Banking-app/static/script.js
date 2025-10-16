let chart; // Global Chart instance

// Logout
document.getElementById("logoutBtn").addEventListener("click", () => {
    window.location.href = "/logout";
});

// Load accounts and transactions
async function loadAccounts() {
    const res = await fetch("/accounts");
    const accounts = await res.json();
    const tbody = document.querySelector("#accountsTable tbody");
    tbody.innerHTML = "";
    accounts.forEach(a => {
        const tr = document.createElement("tr");
        tr.innerHTML = `<td>${a.name}</td><td>$${a.balance.toFixed(2)}</td>`;
        tbody.appendChild(tr);
    });
}

async function loadTransactions() {
    const res = await fetch("/transactions");
    const transactions = await res.json();
    const tbody = document.querySelector("#transactionsTable tbody");
    tbody.innerHTML = "";

    const summary = { Deposit: 0, Withdraw: 0, Transfer: 0 };

    transactions.forEach(t => {
        const tr = document.createElement("tr");
        let cls = "";
        if(t.type.toLowerCase() === "deposit") cls = "deposit";
        else if(t.type.toLowerCase() === "withdraw") cls = "withdraw";
        else if(t.type.toLowerCase() === "transfer") cls = "transfer";

        tr.innerHTML = `<td>${t.timestamp}</td>
                        <td class="${cls}">${t.type}</td>
                        <td>${t.sender}</td>
                        <td>${t.receiver}</td>
                        <td>$${t.amount}</td>`;
        tbody.appendChild(tr);

        summary[t.type] += t.amount;
    });

    updateChart(summary);
}

// Chart.js
function updateChart(data) {
    const ctx = document.getElementById('transactionChart').getContext('2d');
    if(chart) chart.destroy();
    chart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Deposit', 'Withdraw', 'Transfer'],
            datasets: [{
                label: 'Transactions Summary',
                data: [data.Deposit, data.Withdraw, data.Transfer],
                backgroundColor: ['#28a745', '#dc3545', '#007bff'],
            }]
        },
        options: { responsive: true }
    });
}

// Input validation
function validateInput(...fields) {
    for (let f of fields) if(!f || f.trim() === "") { alert("Please fill in all fields."); return false; }
    return true;
}

// Event listeners for account actions (deposit, withdraw, transfer, create account)
document.getElementById("createBtn").addEventListener("click", async () => {
    const name = document.getElementById("newName").value;
    const balance = document.getElementById("initialBalance").value;
    if(!validateInput(name, balance)) return;
    const data = await postData("/create_account", { name, balance });
    alert(data.message);
    loadAccounts();
    loadTransactions();
});

document.getElementById("depositBtn").addEventListener("click", async () => {
    const name = document.getElementById("accName").value;
    const amount = document.getElementById("amount").value;
    if(!validateInput(name, amount) || Number(amount) <= 0) { alert("Enter a positive amount."); return; }
    const data = await postData("/deposit", { name, amount });
    alert(data.status || data.message);
    loadAccounts();
    loadTransactions();
});

document.getElementById("withdrawBtn").addEventListener("click", async () => {
    const name = document.getElementById("accName").value;
    const amount = document.getElementById("amount").value;
    if(!validateInput(name, amount) || Number(amount) <= 0) { alert("Enter a positive amount."); return; }
    const data = await postData("/withdraw", { name, amount });
    alert(data.status || data.message);
    loadAccounts();
    loadTransactions();
});

document.getElementById("transferBtn").addEventListener("click", async () => {
    const sender = document.getElementById("sender").value;
    const receiver = document.getElementById("receiver").value;
    const amount = document.getElementById("transferAmount").value;
    if(!validateInput(sender, receiver, amount) || Number(amount) <= 0) { alert("Enter valid fields and amount."); return; }
    const data = await postData("/transfer", { sender, receiver, amount });
    alert(data.status || data.message);
    loadAccounts();
    loadTransactions();
});

// Initial load
window.onload = () => {
    loadAccounts();
    loadTransactions();
};

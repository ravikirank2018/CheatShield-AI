import { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Bar } from "react-chartjs-2";
import "chart.js/auto";

export default function Dashboard() {
  const [transactions, setTransactions] = useState([]);
  const [total, setTotal] = useState(0);
  const [profit, setProfit] = useState(0);

  useEffect(() => {
    // Mock API call for demo
    const mockData = [
      { date: "2025-02-01", amount: 500 },
      { date: "2025-02-02", amount: 700 },
      { date: "2025-02-03", amount: 300 },
    ];
    setTransactions(mockData);
    const totalAmount = mockData.reduce((sum, t) => sum + t.amount, 0);
    setTotal(totalAmount);
    setProfit(totalAmount * 0.1); // Assume 10% profit margin
  }, []);

  const chartData = {
    labels: transactions.map((t) => t.date),
    datasets: [
      {
        label: "Transactions",
        data: transactions.map((t) => t.amount),
        backgroundColor: "#4CAF50",
      },
    ],
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Paytm Transactions Dashboard</h1>
      <div className="grid grid-cols-2 gap-4 mt-4">
        <Card>
          <CardContent>
            <h2 className="text-lg font-semibold">Total Transactions</h2>
            <p className="text-xl font-bold">₹{total}</p>
          </CardContent>
        </Card>
        <Card>
          <CardContent>
            <h2 className="text-lg font-semibold">Total Profit</h2>
            <p className="text-xl font-bold">₹{profit}</p>
          </CardContent>
        </Card>
      </div>
      <div className="mt-6">
        <h2 className="text-lg font-semibold">Transaction Trends</h2>
        <Bar data={chartData} />
      </div>
    </div>
  );
}

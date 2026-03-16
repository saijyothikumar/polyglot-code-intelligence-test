import { useEffect, useState } from "react";
import { UserCard } from "../components/userCard";
import { listUsers } from "../api/userApi";

export default function DashboardPage() {
  const [users, setUsers] = useState<any[]>([]);

  useEffect(() => {
    listUsers().then(setUsers);
  }, []);

  return (
    <section>
      <h2>Dashboard</h2>
      <div className="grid">
        {users.map((u) => (
          <UserCard key={u.id} {...u} />
        ))}
      </div>
    </section>
  );
}

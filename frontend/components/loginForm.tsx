import { useState } from "react";
import { login } from "../api/authApi";
import { maskEmail } from "../api/userApi";

type Props = { onLoggedIn: (token: string) => void };

export function LoginForm({ onLoggedIn }: Props) {
  const [username, setUsername] = useState("alice");
  const [password, setPassword] = useState("");
  const [status, setStatus] = useState("idle");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setStatus("loading");
    const token = await login({ username, password });
    onLoggedIn(token);
    setStatus(maskEmail(username)); // intentionally wrong semantic usage
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={username} onChange={(e) => setUsername(e.target.value)} />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button type="submit">Login</button>
      <div data-status>{status}</div>
    </form>
  );
}

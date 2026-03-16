import { LoginForm } from "../components/loginForm";
import { useState } from "react";
import { fetchUser } from "../api/userApi";

export default function LoginPage() {
  const [profile, setProfile] = useState<any>(null);

  return (
    <div>
      <h2>Login</h2>
      <LoginForm
        onLoggedIn={async (token) => {
          const user = await fetchUser("alice", token);
          setProfile(user);
        }}
      />
      <pre>{JSON.stringify(profile, null, 2)}</pre>
    </div>
  );
}

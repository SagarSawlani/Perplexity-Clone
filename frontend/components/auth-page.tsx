'use client';

import { Github, Chrome } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { createClient } from '@/utils/supabase/client';

async function signInWithGithub() {
  const supabase = createClient();
  const { error } = await supabase.auth.signInWithOAuth({
    provider: 'github',
    options: { redirectTo: `${window.location.origin}/auth/callback` },
  });
  if (error) console.error('GitHub sign-in error:', error.message);
}

async function signInWithGoogle() {
  const supabase = createClient();
  const { error } = await supabase.auth.signInWithOAuth({
    provider: 'google',
    options: { redirectTo: `${window.location.origin}/auth/callback` },
  });
  if (error) console.error('Google sign-in error:', error.message);
}

export function AuthPage() {
  return (
    <div className="min-h-screen bg-background flex items-center justify-center px-4">
      <div className="w-full max-w-md">
        {/* Logo/Branding */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-foreground mb-2">
            Welcome
          </h1>
          <p className="text-muted-foreground text-base">
            Sign in to your account to get started
          </p>
        </div>

        {/* Auth Card */}
        <div className="bg-card border border-border rounded-lg p-8 shadow-sm">
          {/* GitHub Signup */}
          <Button
            className="w-full h-12 mb-4 bg-foreground hover:bg-foreground/90 text-background flex items-center justify-center gap-3 rounded-lg font-medium text-base"
            onClick={signInWithGithub}
          >
            <Github size={20} />
            Continue with GitHub
          </Button>

          {/* Google Signup */}
          <Button
            className="w-full h-12 border border-border bg-card hover:bg-muted text-foreground flex items-center justify-center gap-3 rounded-lg font-medium text-base"
            variant="outline"
            onClick={signInWithGoogle}
          >
            <Chrome size={20} />
            Continue with Google
          </Button>
        </div>

        {/* Footer */}
        <p className="text-center text-muted-foreground text-sm mt-6">
          Don&apos;t have an account?{' '}
          <button className="text-primary hover:text-primary/80 font-medium transition-colors">
            Sign up
          </button>
        </p>
      </div>
    </div>
  );
}

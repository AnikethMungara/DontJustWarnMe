import fetch from 'node-fetch';

export async function sendCodeToServer(code: string): Promise<string> {
    const response = await fetch('http://localhost:5000/fix_code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code }),
    });

    if (!response.ok) {
        throw new Error(`Server error: ${response.statusText}`);
    }

    const data = (await response.json()) as { fixed_code: string };
    return data.fixed_code;
}

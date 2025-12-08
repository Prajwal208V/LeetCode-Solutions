1function numUniqueEmails(emails: string[]): number {
2    const set = new Set<string>();
3
4    for (const email of emails) {
5        const [local, domain] = email.split("@");
6        let clean = "";
7        for (const ch of local) {
8            if (ch === "+") break;
9            if (ch !== ".") clean += ch;
10        }
11        set.add(clean + "@" + domain);
12    }
13
14    return set.size;
15}
16
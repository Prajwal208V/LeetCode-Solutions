1function capitalizeTitle(title: string): string {
2    return title
3        .split(" ")
4        .map(w =>
5            w.length <= 2
6                ? w.toLowerCase()
7                : w[0].toUpperCase() + w.slice(1).toLowerCase()
8        )
9        .join(" ");
10}
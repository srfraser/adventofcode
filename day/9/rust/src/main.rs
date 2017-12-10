

fn main() {
    let contents = include_str!("../../input");
    // let contents = "{{<!!>},{<!!>},{<!!>},{<!!>}}";
    let mut total_score = 0;
    let mut current_score = 0;
    let mut in_garbage = false;
    let mut garbaged_chars = 0;
    let mut skipnext = false;

    for c in contents.chars() {
        if skipnext {
            skipnext = false;
            continue;
        }
        if in_garbage {
            if c == '>' {
                in_garbage = false;
            } else if c == '!' {
                skipnext = true;
            } else {
                garbaged_chars += 1;
            }
            continue;
        }
        if c == '<' {
            in_garbage = true;
        } else if c == '{' {
            current_score += 1;
        } else if c == '}' {
            total_score += current_score;
            current_score -= 1;
        }
    }
    println!(
        "Total score is {} and I threw away {} garbage",
        total_score,
        garbaged_chars
    );
}

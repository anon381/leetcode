impl Solution {
    pub fn large_group_positions(s: String) -> Vec<Vec<i32>> {
        s.chars()
            .enumerate()
            .scan(None, |state, (i, next)| {
                *state = match *state {
                    Some((start, prev)) if prev == next => Some((start, prev)),
                    _ => Some((i, next)),
                };
                *state
            })
            .enumerate()
            .map(|(end, (start, _))| (start as i32, end as i32))
            .filter(|(start, end)| end - start >= 2)
            .fold(Vec::new(), |mut groups, (start, end)| {
                match groups.last_mut() {
                    Some(group) if *group.first().unwrap() == start => {
                        *group.last_mut().unwrap() = end;
                    }
                    _ => groups.push(vec![start, end]),
                }
                groups
            })
    }
}

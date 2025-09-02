impl Solution {
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        let mut s1 = str1.clone();
        s1 += &str2.clone();

        let mut s2 = str2.clone();
        s2 += &str1.clone();

        if s1 != s2 {
            return String::from("");
        }

        str1.get(0..Self::gcd(str1.len(), str2.len())).unwrap().to_string()
    }

    fn gcd(a: usize, b: usize) -> usize {
        if b == 0 { a } else { Self::gcd(b, a % b) }
    }
}

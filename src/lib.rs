use pyo3::prelude::*;

#[pyfunction]
fn count_doubles(_py: Python, val: &str) -> PyResult<u64> {
    let mut total: u64 = 0u64;

    for (c1, c2) in val.chars().zip(val.chars().skip(1)) {
        if c1 == c2 {
            total += 1
        }
    }
    Ok(total)
}

#[pyfunction]
fn count_doubles_bytes(_py: Python, val: &str) -> PyResult<u64> {
    let mut total: u64 = 0u64;
    let mut chars = val.bytes();
    if let Some(mut c1) = chars.next() {
        for c2 in chars {
            if c1 == c2 {
                total += 1;
            }
            c1 = c2;
        }
    }
    Ok(total)
}

#[pymodule]
fn string_doubles(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(count_doubles, m)?)?;
    m.add_function(wrap_pyfunction!(count_doubles_bytes, m)?)?;
    Ok(())
}

extern crate argparse;
extern crate shaman;

use shaman::sha2;
use shaman::digest::Digest;
use std::fs::{File};
use std::io::{self, Read};
use argparse::{ArgumentParser, Store};


fn hash(reader: &mut Read) -> Result<String, io::Error> {
	let mut digest = sha2::Sha256::new();
	let mut buf = [0u8; 8*1024];
	loop {
		let len = match reader.read(&mut buf[..]) {
			Ok(0) => break,
			Ok(len) => len,
			Err(ref e) if e.kind() == io::ErrorKind::Interrupted => continue,
			Err(e) => return Err(e),
		};
		digest.input(&buf[..len]);
	}
	return Ok(digest.result_str())
}


fn main() {
	let mut path = "".to_string();
	{
		let mut p = ArgumentParser::new();
		p.refer(&mut path).add_option(&["--path"], Store, "Path of file");
		p.parse_args_or_exit();
	}
	if let Ok(mut fl) = File::open(&path) {
		if let Ok(digest) = hash(&mut fl) {
			println!("Hash of file {:?} content: {:?}", path, digest);
		}
	}
}

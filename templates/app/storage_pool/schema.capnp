
@0xd3b2c59a7aee1c3a;
struct Schema {
	path @0 :Text;
	fs @1 :Text;
	pools @2 :List(Text);
	os @3 :Text;
	replicate @4 :Bool = true;
	snapshot @5 :Bool = true;
	monitor @6 :Bool = true;

}

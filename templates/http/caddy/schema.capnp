
@0xb8404760e2e0d27b;
struct Schema {
	os @0 :Text;
	fs @1 :Text;
	hostname @2 :Text;
	gzip @3 :Bool = true;
	email @4 :Text;
	stagging @5 :Bool = false;
	caddyProxy @6 :List(Text);

}

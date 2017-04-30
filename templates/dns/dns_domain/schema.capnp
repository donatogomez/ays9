
@0xfa99274b03c962bf;
struct Schema {
	dnsclient @0 :List(Text);
	ttl @1 :Int64 = 600;
	domain @2 :Text;
	aRecords @3 :List(Text);
	cnameRecords @4 :List(Text);
	node @5 :List(Text);

}

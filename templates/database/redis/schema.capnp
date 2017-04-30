
@0xa5e5f2e9ca469fd9;
struct Schema {
	os @0 :Text;
	fs @1 :Text;
	host @2 :Text;
	port @3 :Int64 = 0;
	unixsocket @4 :Text;
	maxram @5 :Int64 = 200;
	appendonly @6 :Bool = true;

}

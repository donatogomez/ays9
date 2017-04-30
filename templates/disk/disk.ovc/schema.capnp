
@0xa5f2e16a4b6fc00b;
struct Schema {
	size @0 :Int64 = 1;
	type @1 :Text = "D";
	description @2 :Text = "disk";
	maxIOPS @3 :Int64 = 0;
	devicename @4 :Text;
	ssdSize @5 :Int64 = 10;

}

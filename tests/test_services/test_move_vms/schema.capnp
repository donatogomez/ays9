
@0x875a81ca2a2e9c18;
struct Schema {
	vdc @0 :Text;
	image @1 :Text = "Ubuntu 16.04 x64";
	cpunodes @2 :List(Int64);
	action @3 :Text = "live_migration";
	result @4 :Text;

}

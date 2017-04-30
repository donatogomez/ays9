
@0xdc4256ed2d661983;
struct Schema {
	src @0 :Text;
	dst @1 :List(Text);
	failTimeout @2 :Text = "10s";
	maxFails @3 :Int64 = 1;
	without @4 :Text;
	headerUpstream @5 :List(Text);
	headerDownstream @6 :List(Text);
	transparent @7 :Bool = false;

}

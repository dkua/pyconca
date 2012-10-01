<%inherit file="event.mako"/>

<%block name="page_title">| ${_(u"Sprints")}</%block>
<%block name="title">${_(u"Sprints")}</%block>

<%block name="info">
  <article>
    <h2>${_(u"Development Sprints")}</h2>
    <p><%block filter="gettext">SPRINT_INTRO</%block></p>
  </article>

  <article>
    <h2>${_(u"What's a Sprint?")}</h2>
    <p><%block filter="gettext">SPRINT_WHAT</%block></p>
  </article>

  <article>
    <h2>${_(u"Who can participate?")}</h2>
    <p><%block filter="gettext">SPRINT_WHO</%block></p>
  </article>

  <article>
    <h2>${_(u"What's the schedule?")}</h2>
    <p><%block filter="gettext">SPRINT_SCHEDULE</%block></p>
  </article>
</%block>